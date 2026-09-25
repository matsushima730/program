# -*- coding: utf-8 -*-
"""ナレーションを1文ずつ合成する（Kokoro-82M・オフライン）。

クラウド環境では Gemini TTS（キー無し）も edge-tts（通信先がブロック）も使えないため、
gemini-narration の手順（1文1ファイル・読みの辞書・前後の無音を詰める・書き起こし照合）を
Kokoro で再現している。声: 日本語 jf_alpha / 英語 af_heart（どちらも女性・ERS 版リメイクの女性統一に合わせる）。

    python tts.py ja|en [--force]
出力: build/narr_{lang}/{scene}_{nn}.wav と build/narr_{lang}/lines.json（文・長さ・読み）
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

from content import READINGS_JA, SCENES

ROOT = Path(__file__).parent
VOICE = {"ja": ("jf_alpha", 1.0), "en": ("af_heart", 1.0)}
COMMON_READINGS = Path("/home/user/claude-code-workspace/.claude/skills/gemini-narration/references/readings_ja.json")


def load_readings():
    table = {}
    if COMMON_READINGS.exists():
        table.update({k: v for k, v in json.loads(COMMON_READINGS.read_text(encoding="utf-8")).items() if not k.startswith("_")})
    table.update(READINGS_JA)
    return table


def apply_readings(text, table):
    for k in sorted(table, key=len, reverse=True):
        text = text.replace(k, table[k])
    return text


def trim(x, sr, thr=0.01, pad=0.04):
    idx = np.where(np.abs(x) > thr)[0]
    if len(idx) == 0:
        return x
    a = max(0, idx[0] - int(pad * sr))
    b = min(len(x), idx[-1] + int(pad * sr))
    return x[a:b]


def kana(text):
    """読みの確認用（unidic の発音）。"""
    import fugashi
    tg = fugashi.Tagger()
    out = []
    for w in tg(text):
        f = w.feature
        p = getattr(f, "pron", None) or getattr(f, "kana", None)
        out.append(p if p and p != "*" else w.surface)
    return "".join(out)


def main(lang, force=False):
    from kokoro_onnx import Kokoro
    k = Kokoro(str(ROOT / "models/kokoro-v1.0.onnx"), str(ROOT / "models/voices-v1.0.bin"))
    voice, speed = VOICE[lang]
    out_dir = ROOT / "build" / ("narr_" + lang)
    out_dir.mkdir(parents=True, exist_ok=True)
    table = load_readings() if lang == "ja" else {}
    g2p = None
    if lang == "ja":
        from misaki import ja
        g2p = ja.JAG2P()
    meta = []
    for s in SCENES:
        for i, text in enumerate(s[lang]["lines"], 1):
            lid = "%s_%02d" % (s["id"], i)
            say = apply_readings(text, table) if lang == "ja" else text
            key = hashlib.sha1(("%s|%s|%s|%s" % (voice, speed, say, "v1")).encode()).hexdigest()[:12]
            wav = out_dir / (lid + ".wav")
            keyf = out_dir / (lid + ".key")
            if force or not wav.exists() or not keyf.exists() or keyf.read_text() != key:
                if lang == "ja":
                    ph, _ = g2p(say)
                    samples, sr = k.create(ph, voice=voice, speed=speed, lang="ja", is_phonemes=True)
                else:
                    samples, sr = k.create(say, voice=voice, speed=speed, lang="en-us")
                samples = trim(np.asarray(samples, np.float32), sr)
                sf.write(str(wav), samples, sr, subtype="PCM_16")
                keyf.write_text(key)
                print("gen", lid, "%.2fs" % (len(samples) / sr), flush=True)
            info = sf.info(str(wav))
            meta.append({"id": lid, "scene": s["id"], "text": text, "say": say, "wav": str(wav),
                         "dur": round(info.frames / info.samplerate, 3),
                         "reading": kana(say) if lang == "ja" else ""})
    (out_dir / "lines.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    tot = sum(m["dur"] for m in meta)
    chars = sum(len(re.sub(r"\s", "", m["text"])) for m in meta)
    print("%s: %d lines, speech %.1fs, %.2f chars/s" % (lang, len(meta), tot, chars / tot))


if __name__ == "__main__":
    main(sys.argv[1], "--force" in sys.argv)
