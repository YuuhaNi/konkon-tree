# 機能要求書

## 1. 概要

本機能要求書は、キャンパス内の指定ランドマークを探索し写真を撮影、アップロードするイベント用アプリケーションの具体的な機能を定義します。このアプリケーションは、イベント参加者がQRコードを使用してランドマークを認識し、写真をアップロードして解析することを目的としています。また、スコアリングシステムを通じてゲーム性を提供します。

---

## 2. 機能要件

### 2.1 ユーザーインターフェース

1. **ログイン機能**
   - 既存のチャットアプリ（Line、Facebook Messenger等）を利用したシングルサインオン（SSO）機能。
   - 二要素認証の実装。

2. **ホーム画面**
   - イベント概要、参加方法、スコア確認へのナビゲーションリンクを提供。
   - 現在のスコアと順位の表示。

3. **QRコードスキャナー**
   - アプリからカメラを起動し、QRコードを読み取る機能。
   - 読み取ったQRコードからランドマーク情報を取得し、次のステップへの誘導。

4. **写真撮影とアップロード**
   - QRコードスキャン後、アプリ内カメラで写真撮影。
   - 撮影した写真をサーバーにアップロードする機能。

5. **写真解析と結果表示**
   - アップロード後、写真をサーバーで解析し、ランドマークの正確性を評価。
   - 解析結果とスコアを表示。

6. **スコアリングシステム**
   - 各ランドマークで得られるスコアの計算と表示。
   - リーダーボードの提供。

7. **通知機能**
   - イベント進行状況や重要な更新情報をプッシュ通知で配信。

---

### 2.2 サーバーサイド機能

1. **ユーザー管理**
   - 参加者の情報（ID、認証情報、スコア）の管理。
   - 運営スタッフとシステム管理者のアクセスコントロール。

2. **写真解析**
   - アップロードされた写真の解析機能。
   - 解析結果に基づくスコア計算。

3. **データストレージ**
   - 写真データ、解析結果、スコアデータの保存。
   - 安全なデータバックアップ機能。

4. **スケーラビリティ**
   - 自動スケーリング機能を持ち、ピーク時の負荷に耐える。

5. **バックアップとリストア**
   - 定期的なデータバックアップの取得と迅速なリストア機能。

---

### 2.3 セキュリティ機能

1. **データ暗号化**
   - 保存データと通信データの暗号化。
   - SSL/TLSの利用。

2. **アクセス制御**
   - 役割ベースのアクセス制御（RBAC）の実装。
   - 二要素認証の強制（管理者）。

---

### 2.4 非機能要求への対応

- **パフォーマンス**
  - 応答時間やデータ処理速度の最適化。
- **信頼性**
  - 99.9%以上の稼働率達成。
- **可用性**
  - フェールオーバーと負荷分散機能の実装。
- **保守性**
  - ログ記録と定期的なシステムアップデート。
- **セキュリティ**
  - データ暗号化とアクセス制御の強化。
- **スケーラビリティ**
  - 自動スケーリングとデータストレージの拡張性。
- **ユーザビリティ**
  - 直感的なインターフェースと明確なエラーメッセージ。
- **法規制対応**
  - 個人情報保護法と著作権法の遵守。
- **回復性**
  - 定期的なバックアップと自動復旧システム。

---

この機能要求書は、イベントアプリの設計と開発に必要な基本的な機能を網羅しており、非機能要求と連携し、イベントの成功を支援することを目的としています。この要求書を基に、詳細設計と開発を進めてください。