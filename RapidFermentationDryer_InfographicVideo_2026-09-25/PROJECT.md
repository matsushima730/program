# 急速発酵乾燥装置 解説動画（図解版・クラウド制作）— 案件カルテ

- 作成日: 2026-09-25（Claude Code クラウドセッションで制作）
- 状態: **日本語版・英語版の2本が完成**。タガログ語版は未制作（理由は下の「制約」）
- 依頼: 急速発酵乾燥装置の動画から ERS（Environmental Recycling System）の記述と、元動画のERSロゴの流用をなくす。
  前回より増えたインフォグラフィックの内容も取り込み、コンテンツとして充実させる

## 成果物（`FINAL/`）

| ファイル | 内容 |
|---|---|
| `動画_2026-09-25_急速発酵乾燥装置_図解版_JA.mp4` | 日本語版 8分26秒（1920x1080・30fps・H.264＋AAC・約60MB） |
| `動画_2026-09-25_急速発酵乾燥装置_図解版_JA.srt` | 日本語字幕（焼き込まず別ファイル） |
| `Video_2026-09-25_RapidFermentationDryingSystem_Infographic_EN.mp4` | 英語版 7分41秒（同上・約60MB） |
| `Video_2026-09-25_RapidFermentationDryingSystem_Infographic_EN.srt` | 英語字幕 |
| `contact_sheet_JA.jpg` / `contact_sheet_EN.jpg` | 全18場面の完成状態の一覧（確認用） |
| `share/*_720p.mp4` | 共有用の 720p 版（各30MB未満・2パス。チャットやメールで送る用。作り方は `src/share.sh`） |

## ERS 関連で変えたこと

- **「ERS」「環境リサイクルシステム」「Environmental Recycling System」は台本・画面・字幕のどこにも出さない**。
  装置名は「急速発酵乾燥装置」／英語は device-master の訳に合わせて "Rapid Fermentation and Drying System"
- **元動画の映像を一切使っていない**。ERS ロゴ（緑の三矢印）も、それを描き直した図形も入っていない。
  焼き込みの赤い「ERS」文字が残る心配が原理的にない（全場面を HTML/SVG で新規に描いている）
- 循環図（14場面）は三矢印に見えないよう、5つの点をつなぐ輪（アンバー色）にしている
- 入っているロゴは自社ロゴだけ（結びの場面）。日本語版＝有限会社松和メンテナンス、英語版＝SHOWAM ORGANIC PRODUCTS INC.（brand/guidelines.md の表記ルール）

## 構成（18場面・5章）

| # | 場面 | 章 | 下敷きにした既存の図解テーマ |
|---|---|---|---|
| 01 | 表紙＋目次 | — | — |
| 02 | 水分の多い有機性廃棄物の4つのリスク | 課題 | docs-web 01 高水分原料の4つのリスク |
| 03 | メタンが出るのは酸素が足りないとき | 課題 | GX版 s03 メタンは酸欠から |
| 04 | 処理の全体像（投入→装置→選別→資源化、蒸気・排気の枝） | 仕組み | equipment-ja 01／device-master d06・d10 |
| 05 | 中核となる2つのはたらき（水分除去＋土着菌） | 仕組み | equipment-ja 02／GX版 s04 |
| 06 | 減圧と沸点の関係（概念図） | 仕組み | docs-web 08 減圧と沸点 |
| 07 | 装置の断面（ジャケット・中空回転軸・らせん羽根・蒸気出口） | 仕組み | docs-web 03・10／device-master d08 |
| 08 | 乾燥と発酵を切り替える3段階の運転 | 工程と管理 | docs-web 07 |
| 09 | 蒸気から水を回収する流れ | 工程と管理 | docs-web 02・09／equipment-ja 05 |
| 10 | においを広げにくくする流れ | 工程と管理 | docs-web 11 |
| 11 | 密閉処理の3つの出口 | 工程と管理 | equipment-ja 11 |
| 12 | 運転を見守る5つの指標＋品質確認の流れ | 工程と管理 | docs-web 04・05 |
| 13 | 受け入れる原料と資源としての行き先 | 資源化 | equipment-ja 12／device-master d05 |
| 14 | 地域の中で資源がめぐる | 資源化 | equipment-ja 07／device-master d04 |
| 15 | 温室効果ガスの算定範囲 | 資源化 | docs-web 06 |
| 16 | 処理と資源、二つの価値 | 価値 | equipment-ja 09／device-master d11 |
| 17 | 関わる人と、めぐる価値 | 価値 | equipment-ja 13 |
| 18 | 結び（自社ロゴ） | — | — |

図の画像そのものはクラウドに無い（GitHub には台帳とカタログの文字だけ）ため、**各テーマを動く図解として描き直した**。
文字は画像に焼かず HTML で描いているので、文言を直せば全場面が作り直せる（infographic-deck の方式Aの考え方）。

## 数値・表現の扱い

- **処理時間・温度・処理能力・削減量などの数値は入れていない**。資料間で値が割れていて（2〜4時間／24時間、50〜60℃／50〜70℃ など）、
  equipment-ja の QA_REPORT で「要仕様確認」とされているため
- 「100度」は高い山の上での水の沸点の説明（一般的な物理）として一度だけ使った
- 「排水ゼロ」「100%肥料化」など強い言い切りは使わない。水・熱の再利用は「設置場所の条件に合わせて検討」、
  GHG は「案件ごとにこの範囲で算定」で通した（rapid-fermentation-gx-v3-video の判断に合わせる）
- 受入原料・資源化先は「候補」とし、「品質試験・法規制・地域のルールで確認」と明記

## 制約（クラウド環境で分かったこと）

- ナレーションの標準は gemini-narration（Gemini TTS・Charon）だが、クラウドに `GEMINI_API_KEY` が無く、
  edge-tts の通信先（speech.platform.bing.com）もネットワーク制限で使えない。
  → **オフラインの Kokoro-82M**（GitHub 配布のモデル）で合成した。声は日本語 jf_alpha／英語 af_heart（女性）
- 書き起こし照合（gemini-narration の手順3）は faster-whisper の配布元に届かないため、
  **sherpa-onnx（日本語 ReazonSpeech／英語 whisper base.en）で代替**。読み違いは「二本立て」「市場」の2か所を辞書で直した。
  残った要確認は日英とも各1文で、どちらも認識側の誤り（音声は正しい）と確認済み
- Kokoro はタガログ語に対応していないため、**タガログ語版は作っていない**
- BGM は外部素材なしで合成（F長調・96BPM、`src/bgm.py`）。音量は narration_mix.py の既定（BGM -22 LUFS、語りの間は -10dB、仕上げ -16 LUFS／TP -2.0）

## 納品前QAの結果（2026-09-25）

| 項目 | 日本語版 | 英語版 |
|---|---|---|
| 尺・解像度 | 506.0秒・1920x1080・30fps | 461.3秒・1920x1080・30fps |
| 音量（仕上げ） | -16.0 LUFS／TP -2.0 dBFS | -16.0 LUFS／TP -1.8 dBFS |
| 音声の途切れ（-45dB・2秒以上） | なし（BGM が全編に入っている） | なし |
| ナレーションの重なり・はみ出し | なし（narration_mix.py の警告なし） | なし |
| 書き起こし照合 | 要確認1文＝認識側の誤り（音声は正しい） | 要確認1文＝同左 |
| 全編5秒おきの目視（ERS 表記・ロゴ・文字切れ） | 問題なし | 問題なし |
| 字幕・台本の禁止語（ERS／環境リサイクル／Environmental Recycling） | なし | なし |
| グリフ欠落 | BIZ UDPゴシックに無い「₂」「₄」だけ代替フォントで表示（□にはならないことを拡大で確認） | 同左 |

キーフレームは1秒間隔（-g 30）。HyperFrames に埋め込むなら -g 15 で再エンコードする。

## 再ビルド手順（`src/`）

```bash
pip install kokoro-onnx soundfile pyopenjtalk fugashi jaconv mojimoji addict regex num2words scipy pillow sherpa-onnx
pip install --no-deps misaki        # unidic-lite はビルドが通らないので、sdist を展開して site-packages に置く
# モデル: kokoro-v1.0.onnx / voices-v1.0.bin（github.com/thewh1teagle/kokoro-onnx の releases）→ src/models/
python content.py                  # 台本と画面文言 → build/content.json（禁止語の検査つき）
python tts.py ja && python tts.py en          # 1文ずつ合成（変えた文だけ作り直す）
python asr_check.py ja && python asr_check.py en   # 書き起こし照合 → build/narr_*/check.md
python timing.py ja && python timing.py en    # 場面の尺と文の開始時刻
node render.js ja stills           # 確認用の静止画（build/stills_ja）
./render_lang.sh ja                # 3並列で撮影→build/silent_ja.mp4
python finalize.py ja 出力.mp4 出力.srt   # BGM 合成・ナレーション合成・字幕
```

- フォント（BIZ UDPゴシック・SIL OFL）は `web/` に置く：
  `https://raw.githubusercontent.com/googlefonts/morisawa-biz-ud-gothic/main/fonts/ttf/BIZUDPGothic-{Regular,Bold}.ttf`
- `tts.py` の共通読み辞書と `finalize.py` の narration_mix.py は、workspace を `/home/user/claude-code-workspace` に clone した前提の絶対パス。
  ローカル（G:\Claude Code）で回すときはこの2か所のパスを直す
- 文言の修正は `content.py` だけ。図の配置は `web/scenes.js`（1場面1関数）
- 撮影は Playwright の Chromium で1コマずつ（約0.1秒/コマ・3並列で日本語版が約9分）
- 音量合成は workspace の `.claude/skills/gemini-narration/scripts/narration_mix.py` をそのまま呼ぶ

## 要確認リスト

1. ナレーションの声が社内標準（Gemini TTS・Charon・男性）と違う。標準に揃えるなら、ローカル環境で
   `gemini-narration` の `gen` を同じ台本（`build/narr_*/lines.json` の text）で回し、`finalize.py` だけやり直せば映像はそのまま使える
2. 表紙・結びの背景（草地の写真）は showam-organic サイトの素材。生成画像の可能性があるため画面に「イメージです」と注記した
3. タガログ語版が必要なら、ローカルで Gemini TTS を使って作る（画面の文言は `content.py` に tl を足す）
4. 受入原料・資源化先の候補（5種ずつ）は device-master・equipment-ja の記載から選んだ。実際に扱う原料に合わせて絞るか確認
