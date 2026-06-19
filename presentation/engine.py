# -*- coding: utf-8 -*-
"""Slide / video frame rendering engine (PIL based, offline, self-contained).

Renders 1920x1080 frames used both for the PDF slide deck and the MP4 videos.
All text uses the IPA Gothic font which covers Japanese + Latin (Tagalog).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080

# --- palette (environmental green theme, matching a SWM board context) ---
GREEN_D = (20, 92, 56)      # deep green
GREEN   = (39, 138, 84)     # primary green
GREEN_L = (120, 190, 150)
ACCENT  = (224, 158, 41)    # warm amber accent
INK     = (28, 38, 32)      # near-black text
GRAY    = (95, 110, 100)
PANEL   = (240, 247, 242)   # light panel
PANEL2  = (228, 240, 232)
WHITE   = (255, 255, 255)
LINE    = (205, 222, 212)
RED     = (185, 70, 60)

FONT_PATH = "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"
FONT_MONO = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"

# IPA Gothic lacks subscript digit glyphs; map them to normal digits.
SUBMAP = {ord(a): b for a, b in zip("₀₁₂₃₄₅₆₇₈₉", "0123456789")}
def S(t):
    return t.translate(SUBMAP) if isinstance(t, str) else t

_cache = {}
def font(size, mono=False):
    key = (size, mono)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(FONT_MONO if mono else FONT_PATH, size)
    return _cache[key]


def new_frame(bg=WHITE):
    return Image.new("RGB", (W, H), bg)


def _tw(d, text, fnt):
    b = d.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0], b[3] - b[1]


def wrap(d, text, fnt, max_w, cjk=False):
    """Wrap text to max width. Word-wrap for Latin, char-wrap for CJK."""
    text = S(text)
    lines = []
    for para in text.split("\n"):
        if para == "":
            lines.append("")
            continue
        if cjk:
            cur = ""
            for ch in para:
                if _tw(d, cur + ch, fnt)[0] <= max_w:
                    cur += ch
                else:
                    lines.append(cur)
                    cur = ch
            if cur:
                lines.append(cur)
        else:
            cur = ""
            for word in para.split(" "):
                trial = word if not cur else cur + " " + word
                if _tw(d, trial, fnt)[0] <= max_w:
                    cur = trial
                else:
                    if cur:
                        lines.append(cur)
                    cur = word
            if cur:
                lines.append(cur)
    return lines


def draw_text(d, xy, text, fnt, fill=INK, anchor=None):
    d.text(xy, S(text), font=fnt, fill=fill, anchor=anchor)


def draw_para(d, x, y, text, fnt, max_w, fill=INK, cjk=False, lh=1.4, anchor_left=True):
    lines = wrap(d, text, fnt, max_w, cjk=cjk)
    step = int(fnt.size * lh)
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += step
    return y


def rounded(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


# ---------- shared chrome ----------
def header_bar(img, d, kicker, lang_tag=""):
    d.rectangle([0, 0, W, 14], fill=GREEN)
    if kicker:
        d.text((90, 70), kicker, font=font(30), fill=GREEN)
        d.line([90, 120, 90 + _tw(d, kicker, font(30))[0], 120], fill=GREEN_L, width=3)


def footer_bar(img, d, page, total, brand):
    y = H - 70
    d.line([90, y, W - 90, y], fill=LINE, width=2)
    d.text((90, y + 14), brand, font=font(24), fill=GRAY)
    if page is not None:
        d.text((W - 90, y + 14), f"{page} / {total}", font=font(24), fill=GRAY, anchor="ra")


# ---------- slide types ----------
def slide_title(title, subtitle, org, tagline, footer):
    img = new_frame(GREEN_D)
    d = ImageDraw.Draw(img)
    # decorative bands
    d.rectangle([0, 0, W, H], fill=GREEN_D)
    for i, c in enumerate([GREEN, GREEN_L, ACCENT]):
        d.rectangle([0, H - 18 - i * 0, W, H], fill=GREEN_D)
    d.rectangle([0, H - 16, W, H], fill=ACCENT)
    d.rectangle([0, 0, W, 16], fill=ACCENT)
    # leaf accent circle
    d.ellipse([W - 360, -160, W + 160, 360], fill=GREEN)
    d.ellipse([W - 250, -120, W + 120, 260], fill=GREEN_L)
    d.text((140, 250), org, font=font(34), fill=GREEN_L)
    y = 330
    for ln in wrap(d, title, font(78), 1500, cjk=True):
        d.text((140, y), ln, font=font(78), fill=WHITE)
        y += 96
    y += 20
    for ln in wrap(d, subtitle, font(40), 1450, cjk=True):
        d.text((140, y), ln, font=font(40), fill=ACCENT)
        y += 56
    d.text((140, H - 150), tagline, font=font(28), fill=GREEN_L)
    d.text((140, H - 105), footer, font=font(24), fill=(180, 205, 190))
    return img


def slide_section(no, title, subtitle, footer, page, total, brand):
    img = new_frame(PANEL)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 26, H], fill=GREEN)
    d.rectangle([26, 0, 40, H], fill=ACCENT)
    d.text((150, 360), no, font=font(150), fill=GREEN_L)
    y = 380
    for ln in wrap(d, title, font(70), 1300, cjk=True):
        d.text((420, y), ln, font=font(70), fill=GREEN_D)
        y += 88
    y += 16
    for ln in wrap(d, subtitle, font(34), 1250, cjk=True):
        d.text((422, y), ln, font=font(34), fill=GRAY)
        y += 48
    footer_bar(img, d, page, total, brand)
    return img


def _title_block(d, kicker, title):
    if kicker:
        d.text((90, 64), kicker, font=font(28), fill=GREEN)
    y = 104
    lines = wrap(d, title, font(54), W - 180, cjk=True)
    for ln in lines:
        d.text((90, y), ln, font=font(54), fill=GREEN_D)
        y += 66
    d.line([90, y + 6, W - 90, y + 6], fill=LINE, width=3)
    return y + 36


def slide_bullets(kicker, title, bullets, footer, page, total, brand, cjk=True, note=None):
    img = new_frame(WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=GREEN)
    y0 = _title_block(d, kicker, title)
    y = y0 + 20
    for b in bullets:
        lvl = 0
        text = b
        if isinstance(b, tuple):
            lvl, text = b
        bx = 110 + lvl * 60
        cy = y + 22
        if lvl == 0:
            d.ellipse([bx, cy, bx + 18, cy + 18], fill=ACCENT)
        else:
            d.rectangle([bx + 2, cy + 6, bx + 16, cy + 10], fill=GREEN_L)
        fnt = font(36 if lvl == 0 else 31)
        col = INK if lvl == 0 else GRAY
        yy = draw_para(d, bx + 40, y, text, fnt, W - bx - 200, fill=col, cjk=cjk, lh=1.32)
        y = yy + (20 if lvl == 0 else 12)
    if note:
        d.rectangle([90, H - 175, W - 90, H - 110], fill=PANEL)
        d.rectangle([90, H - 175, 98, H - 110], fill=ACCENT)
        draw_para(d, 120, H - 168, note, font(25), W - 240, fill=GRAY, cjk=cjk, lh=1.3)
    footer_bar(img, d, page, total, brand)
    return img


def slide_bignum(kicker, title, number, unit, caption, sub, footer, page, total, brand, cjk=True):
    img = new_frame(GREEN_D)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=ACCENT)
    if kicker:
        d.text((90, 80), kicker, font=font(30), fill=GREEN_L)
    y = 130
    for ln in wrap(d, title, font(50), W - 180, cjk=True):
        d.text((90, y), ln, font=font(50), fill=WHITE)
        y += 62
    # big number centered
    d.text((W // 2, 520), number, font=font(230), fill=ACCENT, anchor="mm")
    d.text((W // 2, 660), S(unit), font=font(46), fill=GREEN_L, anchor="mm")
    yy = 740
    for ln in wrap(d, caption, font(40), W - 300, cjk=True):
        d.text((W // 2, yy), ln, font=font(40), fill=WHITE, anchor="ma")
        yy += 54
    if sub:
        yy += 10
        for ln in wrap(d, sub, font(28), W - 300, cjk=True):
            d.text((W // 2, yy), ln, font=font(28), fill=GREEN_L, anchor="ma")
            yy += 38
    d.text((90, H - 60), footer, font=font(22), fill=(150, 185, 165))
    d.text((W - 90, H - 60), f"{page} / {total}", font=font(22), fill=(150, 185, 165), anchor="ra")
    return img


def slide_process(kicker, title, steps, footer, page, total, brand, cjk=True, caption=None):
    """Horizontal process flow with arrow-connected boxes."""
    img = new_frame(WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=GREEN)
    y0 = _title_block(d, kicker, title)
    n = len(steps)
    gap = 36
    box_w = (W - 180 - gap * (n - 1)) // n
    box_h = 420
    top = y0 + 60
    x = 90
    for i, (head, lines, tone) in enumerate(steps):
        fill = PANEL if tone == 0 else (PANEL2 if tone == 1 else (250, 243, 226))
        bar = GREEN if tone == 0 else (GREEN_D if tone == 1 else ACCENT)
        rounded(d, [x, top, x + box_w, top + box_h], 22, fill=fill)
        d.rectangle([x, top, x + box_w, top + 70], fill=bar)
        rounded(d, [x, top, x + box_w, top + 70], 22, fill=bar)
        d.rectangle([x, top + 40, x + box_w, top + 70], fill=bar)
        d.text((x + box_w // 2, top + 35), head, font=font(30), fill=WHITE, anchor="mm")
        yy = top + 100
        for ln in lines:
            for w in wrap(d, ln, font(27), box_w - 50, cjk=cjk):
                d.text((x + 26, yy), w, font=font(27), fill=INK)
                yy += 38
            yy += 8
        if i < n - 1:
            ax = x + box_w + gap // 2
            ay = top + box_h // 2
            d.polygon([(ax - 14, ay - 18), (ax + 14, ay), (ax - 14, ay + 18)], fill=ACCENT)
        x += box_w + gap
    if caption:
        draw_para(d, 90, top + box_h + 40, caption, font(30), W - 180, fill=GRAY, cjk=cjk, lh=1.35)
    footer_bar(img, d, page, total, brand)
    return img


def slide_two_col(kicker, title, left_head, left, right_head, right, footer, page, total, brand, cjk=True):
    img = new_frame(WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=GREEN)
    y0 = _title_block(d, kicker, title)
    top = y0 + 30
    colw = (W - 180 - 50) // 2
    for idx, (head, items, x) in enumerate([(left_head, left, 90), (right_head, right, 90 + colw + 50)]):
        rounded(d, [x, top, x + colw, H - 110], 20, fill=PANEL)
        d.rounded_rectangle([x, top, x + colw, top + 74], radius=20, fill=GREEN if idx == 0 else GREEN_D)
        d.rectangle([x, top + 40, x + colw, top + 74], fill=GREEN if idx == 0 else GREEN_D)
        d.text((x + 30, top + 20), head, font=font(34), fill=WHITE)
        yy = top + 110
        for it in items:
            cy = yy + 16
            d.ellipse([x + 30, cy, x + 44, cy + 14], fill=ACCENT)
            yy = draw_para(d, x + 62, yy, it, font(30), colw - 100, fill=INK, cjk=cjk, lh=1.3) + 14
    footer_bar(img, d, page, total, brand)
    return img


def slide_table(kicker, title, headers, rows, footer, page, total, brand, cjk=True, note=None):
    img = new_frame(WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=GREEN)
    y0 = _title_block(d, kicker, title)
    top = y0 + 30
    ncol = len(headers)
    x0 = 90
    tw = W - 180
    # column weights
    cw = [tw // ncol] * ncol
    rowh = 78
    # header
    d.rounded_rectangle([x0, top, x0 + tw, top + rowh], radius=12, fill=GREEN_D)
    d.rectangle([x0, top + 20, x0 + tw, top + rowh], fill=GREEN_D)
    cx = x0
    for i, htxt in enumerate(headers):
        d.text((cx + 24, top + rowh // 2), htxt, font=font(30), fill=WHITE, anchor="lm")
        cx += cw[i]
    y = top + rowh
    for r, row in enumerate(rows):
        bg = WHITE if r % 2 == 0 else PANEL
        d.rectangle([x0, y, x0 + tw, y + rowh], fill=bg)
        cx = x0
        for i, cell in enumerate(row):
            col = INK
            fnt = font(28)
            if i == 0:
                fnt = font(28)
                col = GREEN_D
            lines = wrap(d, cell, fnt, cw[i] - 40, cjk=cjk)
            ty = y + rowh // 2 - (len(lines) - 1) * 18
            for ln in lines:
                d.text((cx + 24, ty), ln, font=fnt, fill=col, anchor="lm")
                ty += 36
            cx += cw[i]
        y += rowh
    d.rectangle([x0, top, x0 + tw, y], outline=LINE, width=2)
    if note:
        draw_para(d, 90, y + 24, note, font(24), W - 180, fill=GRAY, cjk=cjk, lh=1.3)
    footer_bar(img, d, page, total, brand)
    return img


# ---------- video helpers ----------
def video_scene(kind, **kw):
    """Render a single video frame. kind drives the layout."""
    if kind == "title":
        img = new_frame(GREEN_D)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W, 16], fill=ACCENT)
        d.rectangle([0, H - 16, W, H], fill=ACCENT)
        d.ellipse([-200, H - 300, 300, H + 200], fill=GREEN)
        y = 380
        for ln in wrap(d, kw["title"], font(86), 1500, cjk=True):
            d.text((140, y), ln, font=font(86), fill=WHITE); y += 108
        y += 20
        for ln in wrap(d, kw.get("subtitle", ""), font(44), 1450, cjk=True):
            d.text((140, y), ln, font=font(44), fill=ACCENT); y += 60
        if kw.get("brand"):
            d.text((140, H - 110), kw["brand"], font=font(28), fill=GREEN_L)
        return img
    if kind == "big":
        img = new_frame(GREEN_D)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W, 16], fill=ACCENT)
        for ln_i, ln in enumerate(wrap(d, kw["top"], font(48), W - 240, cjk=True)):
            d.text((W // 2, 170 + ln_i * 60), ln, font=font(48), fill=WHITE, anchor="ma")
        d.text((W // 2, 540), kw["number"], font=font(260), fill=ACCENT, anchor="mm")
        d.text((W // 2, 700), S(kw.get("unit", "")), font=font(50), fill=GREEN_L, anchor="mm")
        yy = 790
        for ln in wrap(d, kw.get("caption", ""), font(40), W - 300, cjk=True):
            d.text((W // 2, yy), ln, font=font(40), fill=WHITE, anchor="ma"); yy += 54
        return img
    if kind == "point":
        img = new_frame(WHITE)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, 30, H], fill=GREEN)
        d.rectangle([30, 0, 46, H], fill=ACCENT)
        if kw.get("step"):
            d.text((140, 150), kw["step"], font=font(34), fill=ACCENT)
        y = 230
        for ln in wrap(d, kw["head"], font(72), W - 320, cjk=True):
            d.text((140, y), ln, font=font(72), fill=GREEN_D); y += 92
        y += 30
        for b in kw.get("bullets", []):
            cy = y + 24
            d.ellipse([150, cy, 172, cy + 22], fill=ACCENT)
            y = draw_para(d, 200, y, b, font(44), W - 360, fill=INK, cjk=True, lh=1.3) + 24
        if kw.get("foot"):
            d.text((140, H - 110), kw["foot"], font=font(28), fill=GRAY)
        return img
    if kind == "flow":
        # reuse process slide layout w/o footer
        img = slide_process(kw.get("kicker", ""), kw["title"], kw["steps"], "", None, 0, "",
                            cjk=True, caption=kw.get("caption"))
        return img
    raise ValueError(kind)
