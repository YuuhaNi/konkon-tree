# 非機能要求書

## 1. パフォーマンス要件
- **応答時間**: アプリはユーザー操作（イベントガイドの起動、写真のアップロード、スコアの表示）に対して1秒以内の応答を提供する。
- **スループット**: システムはピーク時に同時に1000人の参加者がイベントアプリを利用することに耐えることができる。
- **データ転送速度**: 写真のアップロードと解析の完了までの時間は最大5秒以内とする。

## 2. 信頼性要件
- **稼働時間**: イベント期間中の稼働時間は99.9%以上であること。
- **障害対応**: システムの障害発生時は予備の技術サポートチームが10分以内に対応を開始する。

## 3. 可用性要件
- **システム稼動時間**: システムはイベント期間中24時間稼働し、適宜バックアップサーバーが用意される。
- **メンテナンス時間**: メンテナンス作業はイベント時間外に実施し、ユーザーに影響が出ないよう配慮する。

## 4. セキュリティ要件
- **データ保護**: 参加者のデータ（写真、活動履歴、スコア）は暗号化される。
- **アクセス制御**: アクセス権限は最小限に設定し、運営スタッフと技術サポートチームのみが管理機能を持つ。
- **認証と認可**: アプリの利用には既存のチャットアプリの認証情報を利用し、二要素認証を導入する。

## 5. スケーラビリティ要件
- **ユーザーの増加対応**: 情報の並列処理を可能とし、ユーザーが増加しても応答速度が低下しないよう、サーバーの自動スケーリングを実装する。
- **データストレージの拡張性**: 写真や解析データの増加にも対応できるよう、自動的にデータストレージを拡張する機能を持つ。

## 6. 保守性要件
- **コードの可読性**: コードは他の開発者が理解しやすい形でコメントを付けること。
- **ログの記録**: システムの動作状況やエラーログを詳細に記録し、ログ解析ツールを使用して迅速な障害特定を可能にする。
- **アップデートの容易さ**: システムの更新や修正が容易に行える仕組みを設ける。

## 7. 移植性要件
- **クロスプラットフォーム対応**: イベントアプリは主要なモバイルOS（iOS, Android）で同様に動作する。
- **チャットアプリ間の互換性**: イベントアプリは複数の既存チャットアプリとの互換性を持ち、スムーズに連携できる。

## 8. ユーザビリティ要件
- **インターフェースの直感性**: イベントアプリのインターフェースは直感的で使いやすく、短時間の説明で理解できるものとする。
- **エラーメッセージの明確さ**: ユーザーが操作ミスをした際に表示されるエラーメッセージは明確で具体的な対処方法を提供する。

## 9. 法規制対応
- **個人情報保護法の遵守**: 参加者のデータは個人情報保護法に基づき適切に管理する。
- **著作権の遵守**: イベントで使用する画像、テキスト、その他素材は全て著作権を尊重し、適切な使用許諾を得た上で利用する。

## 10. 回復性要件
- **データバックアップ**: 毎時間データバックアップを取得し、問題発生時には直近のバックアップからのリストアが可能であること。
- **自動復旧システム**: システム障害発生時に自動で復旧を開始する仕組みを導入する。

以上の非機能要求は、本プロジェクトの円滑な実行と最終的な成功に向け、堅固な土台を提供するものである。