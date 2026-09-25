# -*- coding: utf-8 -*-
"""無音の映像にナレーションと BGM を載せ、字幕（SRT）を書く。

音量・ダッキングは gemini-narration スキルの narration_mix.py をそのまま使う
（ナレーション -16 LUFS 相当／BGM -22 LUFS・語りの間は 10dB 下げる／仕上げ TP -2.0）。
字幕は英語にも対応させるため、ここで文を区切って書く（1枚 2行まで）。

    python finalize.py ja|en 出力.mp4 出力.srt
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
MIX = Path("/home/user/claude-code-workspace/.claude/skills/gemini-narration/scripts/narration_mix.py")


def chunks(text, lang):
    if lang == "ja":
        parts = [p for p in re.split(r"(?<=[。！？])", text) if p]
        out = []
        for p in parts:
            if len(p) <= 32:
                out.append(p); continue
            cur = ""
            for q in [x for x in re.split(r"(?<=、)", p) if x]:
                if cur and len(cur) + len(q) > 32:
                    out.append(cur); cur = q
                else:
                    cur += q
            if cur:
                out.append(cur)
        return [x.rstrip("、") for x in out]
    parts = [p.strip() for p in re.split(r"(?<=[.!?;:])\s+", text) if p.strip()]
    out = []
    for p in parts:
        if len(p) <= 84:
            out.append(p); continue
        cur = ""
        for q in [x.strip() for x in re.split(r"(?<=,)\s+", p) if x.strip()]:
            if cur and len(cur) + 1 + len(q) > 84:
                out.append(cur); cur = q
            else:
                cur = (cur + " " + q).strip()
        if cur:
            out.append(cur)
    return out


def wrap_en(s, width=42):
    if len(s) <= width:
        return s
    words, best = s.split(), None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        score = max(len(a), len(b))
        if best is None or score < best[0]:
            best = (score, a + "\n" + b)
    return best[1]


def wrap_ja(s, limit=20):
    """20字を超える字幕は、中央に近い読点で2行に分ける。"""
    if len(s) <= limit:
        return s
    cands = [i + 1 for i, ch in enumerate(s[:-1]) if ch == "、"]
    if not cands:
        return s
    i = min(cands, key=lambda k: abs(k - len(s) / 2))
    return s[:i] + "\n" + s[i:]


def ts(s):
    ms = int(round(s * 1000))
    return "%02d:%02d:%02d,%03d" % (ms // 3600000, ms // 60000 % 60, ms // 1000 % 60, ms % 1000)


def write_srt(lang, cues, lines, path):
    dur = {m["id"]: m["dur"] for m in lines}
    out, n = [], 1
    for c in cues:
        parts = chunks(c["text"], lang)
        w = [max(1, len(p)) for p in parts]
        t = c["start"]
        for p, k in zip(parts, w):
            d = dur[c["id"]] * k / sum(w)
            text = wrap_en(p) if lang != "ja" else wrap_ja(p)
            out += [str(n), "%s --> %s" % (ts(t), ts(t + d - 0.04)), text, ""]
            n += 1
            t += d
    Path(path).write_text("\n".join(out), encoding="utf-8-sig")


def main(lang, out_mp4, out_srt, srt_only=False):
    if srt_only:
        cues = json.loads((ROOT / "build" / ("cues_%s.json" % lang)).read_text(encoding="utf-8"))
        lines = json.loads((ROOT / "build" / ("narr_%s" % lang) / "lines.json").read_text(encoding="utf-8"))
        write_srt(lang, cues, lines, out_srt)
        print("srt", out_srt)
        return
    tl = json.loads((ROOT / "build" / ("timeline_%s.json" % lang)).read_text(encoding="utf-8"))
    cues = json.loads((ROOT / "build" / ("cues_%s.json" % lang)).read_text(encoding="utf-8"))
    lines = json.loads((ROOT / "build" / ("narr_%s" % lang) / "lines.json").read_text(encoding="utf-8"))
    bgm = ROOT / "build" / ("bgm_%s.wav" % lang)
    subprocess.run([sys.executable, str(ROOT / "bgm.py"), "%.3f" % tl["total"], str(bgm)], check=True)
    r = subprocess.run([sys.executable, str(MIX), "--video", str(ROOT / "build" / ("silent_%s.mp4" % lang)),
                        "--cues", str(ROOT / "build" / ("cues_%s.json" % lang)), "--bgm", str(bgm), "--out", out_mp4],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(r.stdout, r.stderr)
    r.check_returncode()
    write_srt(lang, cues, lines, out_srt)
    print("srt", out_srt)


if __name__ == "__main__":
    main(*sys.argv[1:4], srt_only="--srt-only" in sys.argv)
