# 機能要求書

## 1. イントロダクション

本機能要求書は、指定されたリスク識別定義書と非機能要求書に基づき、キャンパス探索イベントアプリの具体的な要件を定義し、システムの設計および開発において遵守すべきガイドラインを提供するために作成されました。本文書では、イベントアプリの機能に関する要件を詳細に示します。

## 2. 機能カテゴリ

### 2.1 イベント参加機能

- **QRコードスキャン**
  - 参加者がイベントに参加するためには、QRコードをスキャンしてアプリを起動します。この機能は、イベント前に事前チェックを行い、起動に問題がないことを検証します。
  - **リスク対応**: QRコードが正常に機能しない場合を想定し、事前にバックアップ手順を確立。

- **参加登録**
  - 参加者がアプリを使用する前に必要な登録手続きを行います。名前、メールアドレス、その他必要な情報を収集します。

### 2.2 写真解析とランドマーク識別機能

- **写真撮影とアップロード**
  - 参加者は指定されたランドマークの写真を撮影し、アプリにアップロードします。

- **写真解析**
  - アップロードされた写真を解析し、ランドマークを識別します。識別精度を向上させるために、マシンラーニングモデルを導入します。
  - **リスク対応**: 解析が失敗した場合は、手動による対応手順を準備。

### 2.3 イベントガイド配布機能

- **デジタルガイドの提供**
  - 参加者に対して、イベントのガイドをデジタル形式で提供します。
  - **リスク対応**: ガイドが正しく配布されるように配布状況を確認し、予備を用意。

### 2.4 スコアリング機能

- **自動スコア計算**
  - 各ランドマークで得られたポイントを自動的に集計し、参加者ごとのスコアをリアルタイムで表示します。
  - **リスク対応**: 自動化とは別に、手動でのチェック体制を整備。

### 2.5 ネットワーク接続機能

- **オンライン/オフライン対応**
  - イベント中にネットワーク問題が発生した場合でも、オフラインモードで利用できる機能を提供します。
  - **リスク対応**: ネットワーク接続の事前確認とオフライン機能の準備。

### 2.6 参加者エンゲージメント機能

- **インセンティブシステム**
  - 参加者の積極的な参加を促すために、インセンティブや特典を提供します。
  - **リスク対応**: エンゲージメントの追跡とリアルタイム対策ダッシュボードを提供。

### 2.7 データセキュリティ機能

- **データ暗号化**
  - 全てのユーザーデータを暗号化（AES-256）して保護します。
  - **リスク対応**: 定期的なセキュリティ監査を実施し、データアクセスをモニタリング。

- **アクセス制御**
  - ユーザー認証には二段階認証を導入し、運営スタッフおよび開発チームには役割に応じたアクセス権限を管理します。

### 2.8 サポート機能

- **リアルタイムヘルプ**
  - アプリ使用中に問題が発生した場合、参加者に迅速に対応できるリアルタイムヘルプ機能を提供します。

- **運用サポート**
  - イベント期間中に24時間対応のサポートを提供し、迅速に問題を解決します。

## 3. 最後に

本機能要求書はキャンパス探索イベントアプリの開発において、システムの信頼性、セキュリティ、ユーザビリティを高めるための具体的なガイドラインを提供します。全ての機能要求は、ステークホルダーの期待とプロジェクト成功基準を満たすことを目的としています。今後のシステム設計および開発において、これらの要求を遵守することを確約します。