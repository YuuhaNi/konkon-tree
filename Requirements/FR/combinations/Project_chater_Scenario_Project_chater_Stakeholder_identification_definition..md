# 機能要求書

## 1. 機能要件

### 1.1 導入と開始

1. **運営ステーションでのイベントガイドの配布**
   - イベントガイドの配布機能をアプリに統合し、ユーザーが簡単にアクセスできるようにする。
  
2. **参加者へのアプリの基本的な使い方とイベントのルールの説明**
   - 初回起動時にイベントの概要、基本的な使い方、ルールを表示するチュートリアル機能を提供する。

3. **QRコードの提供**
   - 既存のチャットアプリからイベントアプリをダウンロード・起動するためのQRコード生成及びスキャン機能を提供する。

### 1.2 探索

1. **キャンパス内の指定ランドマークの探索**
   - ランドマークのリストとその地図上の位置を表示する機能。
   - 各ランドマークを訪れたことを確認するGPSトラッキング機能。

2. **写真撮影とアップロード**
   - ランドマークの写真をアプリ内カメラ機能で撮影。
   - 1MB以下のJPEG形式での自動圧縮アップロード機能。
  
3. **写真の自動解析と解説**
   - アップロードされた写真を自動解析し、関連する解説テキストやスコアを表示する機能。
   - AIを使用して、写真の内容を認識し関連情報を提示。

### 1.3 終了と特典付与

1. **活動履歴の確認**
   - 参加者が探索したランドマークや撮影した写真の履歴を表示する機能を提供する。

2. **スコア集計と特典付与**
   - スコアに基づき特典を計算し、参加者に通知する機能。
   - 特典リストと得点に基づく引き換え方法の提供。

## 2. ユーザーインターフェース

### 2.1 直感的な操作
- タッチ操作に直感的に反応するUIデザイン。
- 各機能へのアクセスを容易にするホーム画面のデザイン。

### 2.2 多言語対応
- 日本語および英語での表示を可能にするオプション選択。

## 3. セキュリティ

### 3.1 データ暗号化
- SSL/TLSを使用したデータ暗号化通信。

### 3.2 認証と認可
- ユーザーごとに異なる権限設定を行い、必要最小限の権限のみを付与する。

### 3.3 セキュリティ監査
- リリース前の第三者によるセキュリティ監査を実施。

## 4. システム管理

### 4.1 障害対応
- 障害発生時の迅速な対応と平均復旧時間（MTTR）15分以内を保証するサポート体制の構築。

### 4.2 自動バックアップ
- 全てのデータを1時間ごとに自動でバックアップする機能を実装。

## 5. パフォーマンスとスケーラビリティ

### 5.1 レスポンス時間
- 全ての画面遷移と機能（例：写真のアップロードや解析結果の表示）のレスポンス時間を平均2秒以内に設定。

### 5.2 スループット
- 同時に1000人が利用できるサーバーキャパシティの確保。

### 5.3 拡張性
- クラウドベースのスケーラブルなサーバーインフラを採用し、参加者数の増加に対応。

## 6. 保守性と拡張性

### 6.1 コードのモジュール化
- アプリケーションコードのモジュール化による変更の容易さの確保。

### 6.2 API設計
- RESTful APIの設計とドキュメント提供。

### 6.3 ログとモニタリング
- システムの操作ログとパフォーマンスモニタリングをリアルタイムで行い、異常検知システムを導入。

## 7. ユーザビリティとサポート

### 7.1 サポート窓口
- イベント期間中は24時間対応のサポート窓口を設置。

### 7.2 トレーニング資料
- 運営スタッフ向けにアプリの使い方やよくあるトラブル解決方法に関するトレーニング資料を提供。

## 8. フィードバックと改訂

### 8.1 フィードバック収集
- イベント終了後、参加者と運営スタッフからのフィードバックを収集し、次回イベントの改善に役立てる。

## 9. 環境条件

### 9.1 移動端末でのパフォーマンス
- スマートフォンやタブレットでの全機能の正常動作を保証。

### 9.2 オフライン利用
- 一時的なネットワーク接続不良にも対応できるオフライン機能（写真撮影や一時保存）を実装。

## まとめ
本機能要求書はキャンパス探索イベントの成功に向けた具体的な機能要件を記載しています。これらの要件を基に、参加者が積極的にイベントに関わり、楽しく学ぶ機会を提供しつつ、システムの信頼性とユーザビリティも高めることを目指しています。