# -*- coding: utf-8 -*-
"""場面の尺をナレーションの長さから決め、タイムライン（場面の開始・尺・文の開始）を書き出す。

gemini-narration の決め方に合わせる：
  場面の尺 = 語り出し + 文の長さの合計 + 文間 × (文数-1) + 語り終わり
尺は 1/30 秒単位に丸める（場面ごとに作る mp4 をつないでも時刻がずれないように）。

    python timing.py ja|en   → build/timeline_{lang}.json と build/cues_{lang}.json
"""
import json
import math
import sys
from pathlib import Path

from content import CHAPTERS, SCENES

ROOT = Path(__file__).parent
FPS = 30
LEAD = {"s01_title": 2.0, "s18_closing": 1.2}
TAIL = {"s01_title": 1.6, "s18_closing": 4.0}
DEFAULT_LEAD, DEFAULT_TAIL, GAP = 1.1, 1.4, 0.55


def main(lang):
    lines = json.loads((ROOT / "build" / ("narr_" + lang) / "lines.json").read_text(encoding="utf-8"))
    by_scene = {}
    for m in lines:
        by_scene.setdefault(m["scene"], []).append(m)
    t, scenes, cues = 0.0, [], []
    for s in SCENES:
        ls = by_scene[s["id"]]
        lead, tail = LEAD.get(s["id"], DEFAULT_LEAD), TAIL.get(s["id"], DEFAULT_TAIL)
        cur, sc_cues = lead, []
        for m in ls:
            sc_cues.append({"id": m["id"], "s": round(cur, 3), "d": m["dur"], "text": m["text"]})
            cues.append({"id": m["id"], "start": round(t + cur, 3), "wav": m["wav"], "text": m["text"]})
            cur += m["dur"] + GAP
        dur = cur - GAP + tail
        frames = math.ceil(dur * FPS)
        dur = frames / FPS
        scenes.append({"id": s["id"], "chapter": s["chapter"], "start": round(t, 4), "dur": dur, "frames": frames,
                       "cues": sc_cues, "screen": s[lang]["screen"]})
        t += dur
    # 章ごとの区間（進捗バー用）
    chapters = []
    for c in range(1, len(CHAPTERS[lang])):
        ss = [x for x in scenes if x["chapter"] == c]
        chapters.append({"no": c, "name": CHAPTERS[lang][c], "start": ss[0]["start"], "end": ss[-1]["start"] + ss[-1]["dur"]})
    tl = {"lang": lang, "fps": FPS, "total": t, "chapters": chapters, "scenes": scenes}
    (ROOT / "build" / ("timeline_%s.json" % lang)).write_text(json.dumps(tl, ensure_ascii=False, indent=1), encoding="utf-8")
    (ROOT / "build" / ("cues_%s.json" % lang)).write_text(json.dumps(cues, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%s: %d scenes, total %.1fs (%d:%02d)" % (lang, len(scenes), t, t // 60, t % 60))
    for x in scenes:
        print("  %-22s %6.1f  %5.1fs" % (x["id"], x["start"], x["dur"]))


if __name__ == "__main__":
    main(sys.argv[1])
