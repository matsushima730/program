# 配車管理 (産業廃棄物収集運搬)

産業廃棄物収集運搬業者向けの、トラック配車管理アプリ（Android, Kotlin + Jetpack Compose, ローカルDB のみ）。動くプロトタイプとして、起動時にサンプルデータを投入します。

## 機能

- **配車カレンダー** (タブ 1)
  - 月カレンダー (日曜始まり、土日色分け、配車のある日にドット表示)
  - 選択日の配車カードを一覧表示
  - FAB から新規配車を追加。カードタップで編集 / 削除
  - 配車項目: 車両、ドライバー、排出元、行き先 (処分場/中間処理)、廃棄物種類、発車予定、帰着予定、コンテナ状態 (空/積込中/積載中/荷下し中/帰着済)、備考
- **車両** (タブ 2): プレートナンバー / 車種 / 最大積載量 (kg) / 車両様式 (ダンプ/平ボディ/アームロール/コンテナ車/ウイング/タンク/その他) / メーカー・車名 / 備考
- **ドライバー** (タブ 3): 氏名 / 免許区分 / 電話 / 備考
- **取引先** (タブ 4): 名称 / 区分 (排出事業者 or 処分場・中間処理) / 住所 / 担当者 / 電話 / 備考

## 技術スタック

- Kotlin 2.0.21
- Jetpack Compose (BOM 2024.10.00) + Material 3
- Room 2.6.1 (KSP)
- Navigation Compose 2.8.2
- Lifecycle 2.8.6
- min SDK 26 / target SDK 34
- Java 17 / desugaring 有効 (java.time を minSdk 26 で利用)

## 構成

```
app/src/main/java/com/example/haikibutsuhaisha/
├── HaikibutsuApp.kt          # Application — DBとリポジトリの初期化＋シード
├── MainActivity.kt
├── data/
│   ├── AppDatabase.kt        # Room DB + TypeConverter
│   ├── SeedData.kt           # 初回起動時のサンプル投入
│   ├── entity/               # Truck / Driver / Client / Assignment
│   ├── dao/                  # 4種の DAO
│   └── repository/AppRepository.kt
├── ui/
│   ├── theme/                # Material3 テーマ
│   ├── nav/AppNavGraph.kt    # NavHost + BottomNavigation
│   ├── common/               # 共通 ViewModel ヘルパ / Pickers
│   ├── calendar/             # カレンダー / 配車編集
│   ├── truck/                # 車両 マスタ
│   ├── driver/               # ドライバー マスタ
│   └── client/               # 取引先 マスタ
└── util/DateFmt.kt
```

## 開く / ビルド

### Android Studio で開く（推奨）

1. **Android Studio Hedgehog (2023.1) 以降** で `HaikibutsuHaisha` フォルダを `File > Open`
2. Gradle Sync を実行 (Studio が必要なら Gradle ラッパーを自動生成)
3. エミュレータまたは実機 (API 26+) を選んで Run

### コマンドラインで Wrapper を作る

このリポジトリには `gradle-wrapper.properties` のみ含まれます (バイナリの `gradle-wrapper.jar` は省略)。
ローカルに Gradle 8.10 以上を入れている場合は最初の一回だけ:

```powershell
cd "F:\Claude Code\HaikibutsuHaisha"
gradle wrapper
.\gradlew.bat assembleDebug
```

Android Studio から開く場合は不要 (Studio がラッパー生成と同期を行います)。

## 初回起動時のサンプルデータ

`SeedData.kt` がトラック 3 台、ドライバー 3 名、取引先 4 件 (排出 2 / 処分 2)、本日と翌日に配車 3 件を投入します。
不要なら `HaikibutsuApp.onCreate()` 内の `SeedData.seedIfEmpty(db)` 呼び出しを削除してください。

## 今後の拡張アイデア

- 配車の重複検知 (同一車両 / ドライバーの時間重複バリデーション)
- 月の配車を CSV / マニフェスト形式で出力
- 月別の運行サマリ (車両別 / 取引先別件数)
- 担当ドライバーへの配車予定通知 (FCM など)
- バックアップ / リストア (DB ファイルの export)
- ログイン / マルチユーザ対応 (Firebase Auth + Firestore)
