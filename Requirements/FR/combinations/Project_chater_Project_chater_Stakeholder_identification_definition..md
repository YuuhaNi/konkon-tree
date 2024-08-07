### 機能要求書

#### 1. はじめに
この文書は、キャンパス探索イベントにおけるイベントアプリケーションの機能要求を明確化するためのものです。以下に記載する機能は、プロジェクトの目的とスコープに基づいています。

---

#### 2. 機能要求

##### 2.1 イベントガイドの配布
- **概要**:
  - 運営ステーションでイベントガイドを参加者に配布する機能。
- **詳細説明**:
  - イベント開始時に運営スタッフが物理的なイベントガイドを参加者に配布。
  - イベントガイドにはQRコードが印刷されており、これをスマートフォンで読み取ることで、探索アプリにアクセスできる。

---

##### 2.2 イベントアプリのアクセス
- **概要**:
  - 既存のチャットアプリを使用してイベントアプリにアクセスする機能。
- **詳細説明**:
  - 参加者はQRコードをスキャンし、既存のチャットアプリからイベントアプリに遷移。
  - イベントアプリの認証機能を通じて、参加者を正しく識別および認証。

---

##### 2.3 ランドマーク探索機能
- **概要**:
  - 参加者がキャンパス内の指定ランドマークを探索する機能。
- **詳細説明**:
  - イベントアプリにランドマークのリストとその位置情報が表示される。
  - 参加者は地図機能を使用してランドマークを探索し、特定のランドマーク近くで通知を受け取る。

---

##### 2.4 写真撮影およびアップロード機能
- **概要**:
  - ランドマークでの写真撮影とそのアップロード機能。
- **詳細説明**:
  - イベントアプリ内で直接カメラを起動し、指定されたランドマークの写真を撮影。
  - 撮影後、写真をイベントアプリを通じてサーバーにアップロード。

---

##### 2.5 自動写真解析と解説テキスト表示機能
- **概要**:
  - アップロードされた写真の自動解析を行い、関連する解説テキストやスコアを表示する機能。
- **詳細説明**:
  - アップロードされた写真はバックエンドシステムで自動解析される。
  - 解析に基づき、関連する解説テキストとスコアがリアルタイムで表示される。

---

##### 2.6 スコア管理機能
- **概要**:
  - 参加者のスコアを管理する機能。
- **詳細説明**:
  - 個々のランドマークで取得したスコアを蓄積し、参加者ごとに管理。
  - リーダーボード機能を通じて、参加者間の得点ランキングを表示。

---

##### 2.7 活動履歴の確認機能
- **概要**:
  - イベント終了時に、参加者が自身の活動履歴を確認する機能。
- **詳細説明**:
  - イベントアプリ内に活動履歴確認ページを提供。
  - 参加者は、訪れたランドマークと取得したスコアを確認できる。

---

##### 2.8 特典付与機能
- **概要**:
  - 蓄積されたスコアに基づき、特典を付与する機能。
- **詳細説明**:
  - イベント終了後、運営スタッフがアプリを通じて特典を確認し、参加者にフィジカルまたはデジタルで特典を付与。
  - 特典はスコアに応じて異なる種類が用意される。

---

#### 3. インターフェース要求

##### 3.1 ユーザーインターフェース
- **概要**:
  - アプリ内の全ての機能が直感的に利用できるよう、ユーザーインターフェースを設計。
- **詳細説明**:
  - ホーム画面：イベントの概要と進行状況を表示。
  - ランドマーク地図画面：訪れるべきランドマークの位置情報を表示。
  - カメラ画面：写真撮影およびアップロード機能を提供。
  - 活動履歴画面：過去の探索活動とスコアを一覧で確認。

---

#### 4. データ管理

##### 4.1 データ保存とバックアップ
- **概要**:
  - イベントアプリで取得したデータを安全に保存し、バックアップする機能。
- **詳細説明**:
  - 写真データ、スコアデータは暗号化して保存および転送。
  - データベースは常時バックアップをとり、データ損失を防止。

---

#### 5. セキュリティ

##### 5.1 認証機能
- **概要**:
  - 既存のチャットアプリを通じた認証機能。
- **詳細説明**:
  - 参加者は既存のチャットアプリ（例：LINE、WhatsApp）を通じて認証し、その情報を利用してイベントアプリにログイン。

##### 5.2 データ保護
- **概要**:
  - 写真データとスコアデータのセキュリティを確保する機能。
- **詳細説明**:
  - 写真データとスコアデータは暗号化して保存・転送する。
  - アクセス制御を実装し、管理者と運営スタッフの権限を分離。

---

この機能要求書は、イベント目的と範囲に基づいています。参加者のエンゲージメントを高めるため、全ての機能を効率的かつ直感的に使用できるよう設計されることを目的としています。