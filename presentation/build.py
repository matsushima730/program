# -*- coding: utf-8 -*-
"""Build all deliverables: PDF slide deck, MP4 videos, SRT subtitles, speaker script.

Usage:  python3 build.py
Outputs to output/<lang>/ for lang in ja, en, tl.
"""
import os, sys, subprocess, importlib
import engine as E

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "output")
WORK = os.path.join(ROOT, "work")
FPS = 25

import imageio_ffmpeg
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


# ------------------------------------------------------------------ slides
def build_slides(L):
    """Return list of PIL images for the deck."""
    b = L["brand"]
    cjk = L["cjk"]
    slides = []
    # we don't know total yet; fill page numbers after
    specs = []

    def bullets(key):
        d = L[key]
        return ("bullets", d)

    # title
    t = L["title"]
    slides.append(E.slide_title(t["title"], t["subtitle"], t["org"], t["tagline"], t["footer"]))
    # agenda
    a = L["agenda"]
    specs.append(lambda p, n: E.slide_bullets(a["kicker"], a["title"], a["bullets"], b, p, n, b, cjk=cjk, note=a["note"]))
    # 1 company
    sc = L["sec_company"]; specs.append(lambda p, n, s=sc: E.slide_section(s["no"], s["title"], s["sub"], b, p, n, b))
    c = L["company"]; specs.append(lambda p, n, c=c: E.slide_two_col(c["kicker"], c["title"], c["lh"], c["left"], c["rh"], c["right"], b, p, n, b, cjk=cjk))
    # 2 background
    sb = L["sec_bg"]; specs.append(lambda p, n, s=sb: E.slide_section(s["no"], s["title"], s["sub"], b, p, n, b))
    bg = L["background"]; specs.append(lambda p, n, x=bg: E.slide_bullets(x["kicker"], x["title"], x["bullets"], b, p, n, b, cjk=cjk, note=x["note"]))
    du = L["dual"]; specs.append(lambda p, n, x=du: E.slide_two_col(x["kicker"], x["title"], x["lh"], x["left"], x["rh"], x["right"], b, p, n, b, cjk=cjk))
    # video 1 cue
    q1 = L["cue1"]; specs.append(lambda p, n, s=q1: E.slide_section(s["no"], s["title"], s["sub"], b, p, n, b))
    # 3 technology
    st = L["sec_tech"]; specs.append(lambda p, n, s=st: E.slide_section(s["no"], s["title"], s["sub"], b, p, n, b))
    ts = L["tech_spec"]; specs.append(lambda p, n, x=ts: E.slide_bullets(x["kicker"], x["title"], x["bullets"], b, p, n, b, cjk=cjk, note=x["note"]))
    tp = L["tech_proc"]; specs.append(lambda p, n, x=tp: E.slide_process(x["kicker"], x["title"], x["steps"], b, p, n, b, cjk=cjk, caption=x["caption"]))
    tc = L["tech_cmp"]; specs.append(lambda p, n, x=tc: E.slide_table(x["kicker"], x["title"], x["headers"], x["rows"], b, p, n, b, cjk=cjk, note=x["note"]))
    to = L["tech_out"]; specs.append(lambda p, n, x=to: E.slide_bullets(x["kicker"], x["title"], x["bullets"], b, p, n, b, cjk=cjk, note=x["note"]))
    # 4 ghg
    sg = L["sec_ghg"]; specs.append(lambda p, n, s=sg: E.slide_section(s["no"], s["title"], s["sub"], b, p, n, b))
    gm = L["ghg_method"]; specs.append(lambda p, n, x=gm: E.slide_table(x["kicker"], x["title"], x["headers"], x["rows"], b, p, n, b, cjk=cjk, note=x["note"]))
    gr = L["ghg_result"]; specs.append(lambda p, n, x=gr: E.slide_bignum(x["kicker"], x["title"], x["number"], x["unit"], x["caption"], x["sub"], b, p, n, b, cjk=cjk))
    # 5 model + video 2 cue
    sm = L["sec_model"]; specs.append(lambda p, n, s=sm: E.slide_section(s["no"], s["title"], s["sub"], b, p, n, b))
    q2 = L["cue2"]; specs.append(lambda p, n, s=q2: E.slide_section(s["no"], s["title"], s["sub"], b, p, n, b))
    mf = L["model_flow"]; specs.append(lambda p, n, x=mf: E.slide_process(x["kicker"], x["title"], x["steps"], b, p, n, b, cjk=cjk, caption=x["caption"]))
    fo = L["fs_obj"]; specs.append(lambda p, n, x=fo: E.slide_bullets(x["kicker"], x["title"], x["bullets"], b, p, n, b, cjk=cjk, note=x["note"]))
    fr = L["fs_road"]; specs.append(lambda p, n, x=fr: E.slide_table(x["kicker"], x["title"], x["headers"], x["rows"], b, p, n, b, cjk=cjk))
    po = L["policy"]; specs.append(lambda p, n, x=po: E.slide_bullets(x["kicker"], x["title"], x["bullets"], b, p, n, b, cjk=cjk))
    kp = L["kpi"]; specs.append(lambda p, n, x=kp: E.slide_two_col(x["kicker"], x["title"], x["lh"], x["left"], x["rh"], x["right"], b, p, n, b, cjk=cjk))
    # 6 summary
    su = L["summary"]; specs.append(lambda p, n, x=su: E.slide_bullets(x["kicker"], x["title"], x["bullets"], b, p, n, b, cjk=cjk, note=x["note"]))
    # closing (title style)
    cl = L["closing"]; specs.append(lambda p, n, x=cl: E.slide_title(x["title"], x["subtitle"], x["org"], x["tagline"], x["footer"]))

    total = 1 + len(specs)
    page = 2
    for fn in specs:
        slides.append(fn(page, total))
        page += 1
    return slides


def write_pdf(slides, path):
    first, rest = slides[0], slides[1:]
    first.save(path, "PDF", resolution=150.0, save_all=True, append_images=rest)


# ------------------------------------------------------------------ video
def render_video(scenes, mp4_path, srt_path, lang):
    frames_dir = os.path.join(WORK, f"frames_{lang}_{os.path.basename(mp4_path)}")
    os.makedirs(frames_dir, exist_ok=True)
    # render unique scene images
    concat_lines = []
    srt_entries = []
    t = 0.0
    for i, sc in enumerate(scenes):
        img = E.video_scene(sc["kind"], **{k: v for k, v in sc.items() if k not in ("kind", "dur", "srt")})
        fp = os.path.join(frames_dir, f"s{i:03d}.png")
        img.save(fp)
        dur = sc["dur"]
        concat_lines.append(f"file '{fp}'")
        concat_lines.append(f"duration {dur}")
        srt_entries.append((t, t + dur, sc.get("srt", "")))
        t += dur
    # last frame must be repeated for concat demuxer
    last_fp = os.path.join(frames_dir, f"s{len(scenes)-1:03d}.png")
    concat_lines.append(f"file '{last_fp}'")
    concat_file = os.path.join(frames_dir, "concat.txt")
    with open(concat_file, "w") as f:
        f.write("\n".join(concat_lines))
    # build srt
    def ts(x):
        h = int(x // 3600); m = int((x % 3600) // 60); s = x % 60
        return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")
    with open(srt_path, "w") as f:
        for n, (a, c, txt) in enumerate(srt_entries, 1):
            f.write(f"{n}\n{ts(a)} --> {ts(c)}\n{txt}\n\n")
    # encode mp4
    cmd = [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
           "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-preset", "medium",
           "-crf", "20", "-movflags", "+faststart", mp4_path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:])
        raise RuntimeError("ffmpeg failed for " + mp4_path)
    return t


# ------------------------------------------------------------------ script
def write_script(L, path):
    lines = [f"# {L['deck_title']}", "", f"**{L['brand']}**", "",
             "Speaker script / run-of-show (about 30 minutes). "
             "Slides are presented with two short videos interleaved.", "",
             "---", ""]
    for head, body in L["script"]:
        lines.append(f"## {head}")
        lines.append("")
        lines.append(body)
        lines.append("")
    with open(path, "w") as f:
        f.write("\n".join(lines))


# ------------------------------------------------------------------ main
def main():
    langs = ["ja", "en", "tl"]
    for lang in langs:
        L = importlib.import_module(f"content_{lang}").PACK
        d = os.path.join(OUT, lang)
        os.makedirs(d, exist_ok=True)
        print(f"=== {lang} ===")
        slides = build_slides(L)
        pdf = os.path.join(d, f"deck_{lang}.pdf")
        write_pdf(slides, pdf)
        print("  deck:", pdf, f"({len(slides)} slides)")
        t1 = render_video(L["v1"], os.path.join(d, f"video1_technology_{lang}.mp4"),
                          os.path.join(d, f"video1_technology_{lang}.srt"), lang)
        print(f"  video1: {t1:.0f}s")
        t2 = render_video(L["v2"], os.path.join(d, f"video2_circular_model_{lang}.mp4"),
                          os.path.join(d, f"video2_circular_model_{lang}.srt"), lang)
        print(f"  video2: {t2:.0f}s")
        write_script(L, os.path.join(d, f"script_{lang}.md"))
        print("  script written")


if __name__ == "__main__":
    main()
