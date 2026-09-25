# -*- coding: utf-8 -*-
"""合成したナレーションを書き起こして原稿と照合する（gemini-narration の check の代わり）。

faster-whisper のモデル配布元に届かないため、sherpa-onnx の GitHub 配布モデルを使う。
日本語: ReazonSpeech zipformer / 英語: whisper base.en。
日本語は漢字の当て方の違いで誤検出しないよう、両方を読み（カナ）に直してから比べる。

    python asr_check.py ja|en      → build/narr_{lang}/check.md
"""
import difflib
import json
import re
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).parent
ASR = ROOT / "models/asr"


def recognizer(lang):
    import sherpa_onnx
    if lang == "ja":
        d = ASR / "sherpa-onnx-zipformer-ja-reazonspeech-2024-08-01"
        return sherpa_onnx.OfflineRecognizer.from_transducer(
            encoder=str(d / "encoder-epoch-99-avg-1.int8.onnx"), decoder=str(d / "decoder-epoch-99-avg-1.int8.onnx"),
            joiner=str(d / "joiner-epoch-99-avg-1.int8.onnx"), tokens=str(d / "tokens.txt"), num_threads=4)
    d = ASR / "sherpa-onnx-whisper-base.en"
    return sherpa_onnx.OfflineRecognizer.from_whisper(
        encoder=str(d / "base.en-encoder.int8.onnx"), decoder=str(d / "base.en-decoder.int8.onnx"),
        tokens=str(d / "base.en-tokens.txt"), num_threads=4)


def to_16k(x, sr):
    from scipy.signal import resample_poly
    if x.ndim > 1:
        x = x[:, 0]
    return resample_poly(x, 16000, sr).astype(np.float32) if sr != 16000 else x.astype(np.float32)


_tagger = None


def kana(text):
    global _tagger
    import fugashi
    if _tagger is None:
        _tagger = fugashi.Tagger()
    out = []
    for w in _tagger(text):
        p = getattr(w.feature, "pron", None)
        out.append(p if p and p != "*" else w.surface)
    s = "".join(out)
    s = "".join(chr(ord(c) + 0x60) if "ぁ" <= c <= "ゖ" else c for c in s)   # ひらがな→カタカナ
    return re.sub(r"[^ァ-ヴー]", "", s)


def norm_en(text):
    return re.sub(r"[^a-z0-9 ]", " ", text.lower().replace("-", " ")).split()


def main(lang):
    rec = recognizer(lang)
    lines = json.loads((ROOT / "build" / ("narr_" + lang) / "lines.json").read_text(encoding="utf-8"))
    rows, bad = [], 0
    for m in lines:
        x, sr = sf.read(m["wav"])
        st = rec.create_stream()
        pad = np.zeros(8000, np.float32)                 # 前後 0.5 秒の無音（無いと頭を落とす）
        st.accept_waveform(16000, np.concatenate([pad, to_16k(x, sr), pad, pad]))
        rec.decode_stream(st)
        heard = st.result.text.strip()
        if lang == "ja":
            a, b = kana(m["say"]), kana(heard)
        else:
            a, b = norm_en(m["text"]), norm_en(heard)
        r = difflib.SequenceMatcher(None, a, b).ratio()
        flag = "" if r >= 0.9 else "要確認"
        bad += bool(flag)
        rows.append("| %s | %.2f | %s | %s | %s |" % (m["id"], r, flag, m["text"], heard))
        print("%-26s %.2f %s" % (m["id"], r, flag), flush=True)
    out = ROOT / "build" / ("narr_" + lang) / "check.md"
    out.write_text("| id | 一致度 | 判定 | 原稿 | 聞こえた |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print("要確認 %d / %d → %s" % (bad, len(rows), out))


if __name__ == "__main__":
    main(sys.argv[1])
