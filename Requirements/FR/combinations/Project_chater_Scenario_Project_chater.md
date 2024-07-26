# 機能要求書

## 1. ユーザー登録と認証
### 1.1 ユーザー登録
- **機能**: イベントアプリは既存のチャットアプリとの連携を通じて、ユーザーの登録作業をシンプルにする。
- **詳細**: チャットアプリの認証情報を利用して、追加の情報入力なしにイベントアプリへアクセスできる。

### 1.2 認証
- **機能**: 二要素認証を利用したセキュアなログインが提供される。
- **詳細**: チャットアプリを通じた認証後、さらにワンタイムパスワードを利用した認証を行う。

## 2. イベントガイドの配布
### 2.1 イベントガイド閲覧
- **機能**: イベントガイドをアプリ内で閲覧可能。
- **詳細**: 導入ステップ、探索方法、ルールなどを詳しく説明するセクションを提供。

### 2.2 QRコード利用
- **機能**: チャットアプリから直接イベントアプリを起動するためのQRコードを提供。
- **詳細**: QRコードをスキャンすることで、イベントアプリが即座に起動し、登録済みユーザーとしてイベントに参加可能。

## 3. ランドマーク探索機能
### 3.1 ランドマーク案内
- **機能**: 参加者が探索すべきランドマークの一覧を提供。
- **詳細**: 地図上に各ランドマークの位置を表示し、ナビゲーション機能も付与。

### 3.2 写真撮影およびアップロード
- **機能**: 指定ランドマーク到達時に写真を撮影してアプリ内にアップロード。
- **詳細**: アプリ内カメラ機能から直接写真を撮影、もしくは既存の写真ギャラリーから選択してアップロード可能。

### 3.3 自動解析およびスコア表示
- **機能**: アップロードされた写真の自動解析と解説テキスト、スコアの表示。
- **詳細**: 画像解析アルゴリズムを使用して写真の内容を確認し、適切なスコアと解説を提供。

## 4. アクティビティ管理
### 4.1 活動履歴の保存
- **機能**: 参加者の活動履歴（訪問したランドマーク、撮影した写真、獲得したスコア）を保存。
- **詳細**: 各ユーザーごとに個別の活動履歴を記録し、イベント終了時に総まとめ表示が可能。

### 4.2 成績確認
- **機能**: 参加者がリアルタイムで自分のスコアとランキングを確認。
- **詳細**: スコアボード機能を提供し、トップパフォーマーを表示。

## 5. イベント終了と特典付与
### 5.1 イベント終了チェックイン
- **機能**: イベント終了時に運営ステーションで最終チェックインを行い、活動履歴を確認。
- **詳細**: アプリ内である一定数のランドマークを訪問したか、特定の条件を満たしたかを確認。

### 5.2 特典の付与
- **機能**: 獲得したスコアに応じて特定の賞品やバッジを付与。
- **詳細**: アプリ内で表示される特典リストと物理的な受取手続きの案内を提供。

## 6. イベントのフォローアップ
### 6.1 参加者フィードバック
- **機能**: イベント終了後、参加者からのフィードバックを収集。
- **詳細**: フィードバックフォームをアプリ内に設置し、改善点や感想を記述してもらう。

### 6.2 イベントレポートの生成
- **機能**: イベント全体の統計データを基にしたレポートを生成。
- **詳細**: 参加者の総数、訪問したランドマークの数、総スコア、フィードバックからの重要な指摘などを含む。

## 7. イベントアプリの管理機能
### 7.1 管理者ダッシュボード
- **機能**: イベント運営チーム向けに、リアルタイムの参加者状況やシステムステータスを監視できるダッシュボードを提供。
- **詳細**: 主要なメトリクス（参加者数、写真アップロード数、システム稼働率）をグラフィカルに表示。

### 7.2 トラブルシューティング
- **機能**: 問題発生時に迅速に対応するためのサポートツールを提供。
- **詳細**: ログ解析ツールやエラーレポート機能を備え、問題の素早い特定と解決を支援。

---

以上が「キャンパス探索イベント」用の機能要求書です。この要求書はイベントの円滑な実行とユーザーの満足度向上を目的としています。