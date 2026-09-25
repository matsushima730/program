# -*- coding: utf-8 -*-
"""BGM を合成する（外部素材なし＝権利クリア）。明るく落ち着いた説明動画向け。

F長調・96BPM。和音パッド＋アルペジオ＋ベース＋ごく小さいシェイカー。8小節で1周し、
後半はコード進行を少し変えて単調さを避ける。軽いリバーブ（コムフィルタ）をかける。
音量はナレーション合成側（narration_mix.py）で -22 LUFS に合わせるので、ここでは波形だけ作る。

    python bgm.py 秒数 出力.wav
"""
import sys
import wave

import numpy as np
from scipy.signal import lfilter

SR = 48000
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT
A4 = 440.0
NOTE = {"C": -9, "C#": -8, "D": -7, "Eb": -6, "E": -5, "F": -4, "F#": -3, "G": -2, "Ab": -1, "A": 0, "Bb": 1, "B": 2}


def hz(name, octave):
    return A4 * 2 ** ((NOTE[name] + 12 * (octave - 4)) / 12)


# コード（ルート, 構成音）。2小節ずつ
PROG_A = [("F", ["F", "A", "C"]), ("C", ["C", "E", "G"]), ("D", ["D", "F", "A"]), ("Bb", ["Bb", "D", "F"])]
PROG_B = [("Bb", ["Bb", "D", "F"]), ("F", ["F", "A", "C"]), ("G", ["G", "Bb", "D"]), ("C", ["C", "E", "G"])]


def env(n, a, r, sustain=1.0):
    e = np.ones(n) * sustain
    na, nr = int(a * SR), int(r * SR)
    e[:na] = np.linspace(0, sustain, na)
    e[-nr:] *= np.linspace(1, 0, nr)
    return e


def pad_voice(f, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.zeros(n)
    for det in (-0.0018, 0.0018):
        ff = f * (1 + det)
        x += np.sin(2 * np.pi * ff * t) + 0.25 * np.sin(2 * np.pi * 2 * ff * t) + 0.08 * np.sin(2 * np.pi * 3 * ff * t)
    return x * env(n, 0.9, 1.2) * (1 + 0.05 * np.sin(2 * np.pi * 0.2 * t))


def pluck(f, dur=0.9):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.08) + 0.1 * np.sin(2 * np.pi * 3 * f * t) * np.exp(-t / 0.05)
    return x * np.exp(-t / 0.32) * np.minimum(1, t / 0.004)


def bass(f, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)
    return x * np.exp(-t / 0.9) * np.minimum(1, t / 0.01)


def shaker(dur=0.06, seed=0):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    x = rng.standard_normal(n)
    x = lfilter([1, -1], [1, -0.6], x)          # 高域寄り
    return x * np.exp(-np.arange(n) / SR / 0.018)


def tail(x, sec=0.04):
    """音の終わりを短く絞る（打ち切りのクリックを防ぐ）。"""
    n = min(len(x), int(sec * SR))
    x = x.copy()
    x[-n:] *= np.linspace(1, 0, n)
    return x


def add(buf, x, t0, gain=1.0, pan=0.0):
    x = tail(x)
    i = int(t0 * SR)
    if i >= buf.shape[0]:
        return
    x = x[: buf.shape[0] - i]
    l, r = np.sqrt(0.5 * (1 - pan)), np.sqrt(0.5 * (1 + pan))
    buf[i:i + len(x), 0] += x * gain * l
    buf[i:i + len(x), 1] += x * gain * r


def reverb(x, wet=0.22):
    out = np.zeros_like(x)
    for d, g in ((1557, 0.78), (1617, 0.77), (1491, 0.79), (1422, 0.8), (1277, 0.76), (1356, 0.77)):
        a = np.zeros(d + 1); a[0] = 1; a[d] = -g
        out += lfilter([1], a, x, axis=0)
    out /= 6
    return x * (1 - wet) + out * wet * 0.5


def main(seconds, path):
    total = float(seconds) + 2
    buf = np.zeros((int(total * SR), 2))
    arp_pat = [0, 1, 2, 3, 2, 1, 0, 2]   # 8分音符
    bar, t = 0, 0.0
    while t < total:
        section = (bar // 8) % 4
        prog = PROG_A if section in (0, 2) else PROG_B
        root, tones = prog[(bar // 2) % 4]
        if bar % 2 == 0:
            for k, nm in enumerate(tones):
                add(buf, pad_voice(hz(nm, 3 if k == 0 else 4), 2 * BAR + 1.0), t, 0.09, pan=(k - 1) * 0.3)
            add(buf, bass(hz(root, 2), 2 * BEAT), t, 0.20)
            add(buf, bass(hz(root, 2), 2 * BEAT), t + 2 * BEAT, 0.14)
            add(buf, bass(hz(root, 2), 2 * BEAT), t + BAR, 0.18)
            add(buf, bass(hz(tones[2], 2), 2 * BEAT), t + BAR + 2 * BEAT, 0.13)
        if section != 0 or bar >= 2:                      # 頭の2小節はパッドだけ
            notes = [hz(tones[0], 5), hz(tones[1], 5), hz(tones[2], 5), hz(tones[0], 6)]
            for j, p in enumerate(arp_pat):
                accent = 1.0 if j % 2 == 0 else 0.75
                add(buf, pluck(notes[p]), t + j * BEAT / 2, 0.055 * accent, pan=0.25 if j % 2 else -0.15)
        if section in (1, 2, 3):
            for j in range(8):
                if j % 2 == 1:
                    add(buf, shaker(seed=bar * 8 + j), t + j * BEAT / 2, 0.025, pan=0.4)
        bar += 1
        t += BAR
    # 3/8拍の軽いディレイ（アルペジオの広がり）
    d = int(0.375 * BEAT * 2 * SR)
    dl = np.zeros_like(buf); dl[d:] = buf[:-d] * 0.18
    buf = reverb(buf + dl)
    n = int(float(seconds) * SR)
    buf = buf[:n]
    fi = int(2.0 * SR)
    buf[:fi] *= np.linspace(0, 1, fi)[:, None]
    buf /= np.max(np.abs(buf)) / 0.8
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((buf * 32767).astype(np.int16).tobytes())
    print("bgm", path, "%.1fs" % (n / SR))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
