## 機能要求書

### 1. 概要
この文書は、「キャンパス探索イベント」プロジェクトにおける機能要求を明確に定義します。この機能要求書は、ステークホルダーの関心事と関係性を考慮し、イベントの成功とスムーズな運営を確実にするために策定されました。

### 2. イベントアプリ機能要求

#### 2.1 アカウント管理機能
- **ユーザー登録**:
  - 参加者と運営スタッフが各自アカウントを作成できる機能
  - 必須項目：名前、メールアドレス、パスワード

- **ログイン/ログアウト機能**:
  - 登録済みユーザーがメールアドレスとパスワードでログイン、ログアウトできる機能
  - 多要素認証によるログインのセキュリティ強化

- **パスワードリセット**:
  - パスワードを忘れたユーザーがメールアドレスを使用してパスワードリセットリンクを受け取る機能

#### 2.2 イベント情報表示機能
- **イベント概要**:
  - イベントの目的、スケジュール、会場情報などの基本情報を表示する機能

- **スケジュール管理**: 
  - 詳細なスケジュール（セッション名、時間、場所、講師情報など）を表示する機能

- **通知機能**:
  - イベントの更新情報、セッションの開始や終了の通知をリアルタイムに送信する機能

#### 2.3 ナビゲーション機能
- **地図表示**:
  - イベント会場（キャンパス）の地図を表示し、参加者が現在地と目的地を確認できる機能

- **経路案内**:
  - 現在地から目的地までのルートを示す機能
  - 主要なランドマークや重要ポイントへの行き方を表示

#### 2.4 チャット機能
- **1対1チャット**:
  - 参加者同士や運営スタッフと1対1でチャットができる機能

- **グループチャット**:
  - 同じセッションに参加するユーザー同士でグループチャットができる機能

- **チャット履歴**:
  - チャットの履歴を保存し、後から確認できる機能

#### 2.5 QRコード機能
- **QRコードスキャン**:
  - 参加者が会場内の特定ポイントに置かれたQRコードをスキャンすることで、関連情報を取得できる機能

- **イベント参加証明**:
  - 参加者がスキャンすることで、各セッションへの参加を証明し、ポイントを獲得できる機能

#### 2.6 フォトシェア機能
- **写真アップロード**:
  - 参加者がイベントの写真をアップロードできる機能

- **共有とコメント**:
  - アップロードされた写真に対して、他の参加者がコメントやいいねをつける機能

- **フォトギャラリー**:
  - イベント中に撮影された写真をまとめて閲覧できる機能

#### 2.7 リーダーボード機能
- **ポイントシステム**:
  - 参加者がアクティビティ（QRコードスキャン、セッション参加、チャットなど）を通じてポイントを獲得できる機能

- **ランキング表示**:
  - 獲得ポイントに基づいて参加者のランキングを表示する機能

#### 2.8 評価およびフィードバック機能
- **セッション評価**:
  - 参加したセッションの評価をリアルタイムで行う機能（星評価やコメント）

- **フィードバックフォーム**:
  - イベント全体に対するフィードバックを提供できるフォーム

### 3. 管理者向け機能要求

#### 3.1 スケジュール管理機能
- **セッション管理**:
  - 各セッションの詳細情報（名前、講師、時間、場所など）を作成・編集・削除する機能

#### 3.2 参加者管理機能
- **登録者リスト**:
  - 参加者の登録情報（名前、メールアドレス、参加セッションなど）を閲覧・編集できる機能

- **アクセス権限管理**:
  - 参加者やスタッフのアカウントに対するアクセス権限を設定・変更する機能

#### 3.3 フォト管理機能
- **写真監視**:
  - アップロードされた写真を確認し、不適切なコンテンツが含まれていないかをチェックする機能

#### 3.4 レポート作成機能
- **参加状況レポート**:
  - 各セッションの参加状況、総参加人数などのレポートを生成する機能

- **フィードバックレポート**:
  - 参加者のフィードバックを集計し、レポートを作成する機能

---

この機能要求書は、「キャンパス探索イベント」プロジェクトの成功を確実にするための各種機能要件を明確に定めたものです。これらの機能が効果的に実装されることで、ステークホルダーの満足度向上と円滑なイベント運営が期待されます。