### 非機能要求書 (NFR)

#### 1. パフォーマンス要求
- **応答時間:**
  - イベントアプリは、ユーザー操作に対して遅延なく即座に応答すること。特に、写真のアップロードやスコアの表示は3秒以内に完了するようにする。
- **スループット:**
  - システムは同時に500人の参加者がアプリを使用することを想定し、安定動作を保証する。
- **データ処理速度:**
  - 写真の自動解析とスコア計算は、画像アップロード後10秒以内に完了する。

#### 2. 可用性要求
- **稼働時間:**
  - イベント期間中（開始日から終了日まで）は、アプリの稼働率を99.9%とする。
- **フォールトトレランス:**
  - システム障害時には自動切り替え機能を用意し、最長5分以内にサービスを復旧する。
- **バックアップ:**
  - データベースは常時バックアップを取り、万が一のデータ損失を最小限に抑える。

#### 3. セキュリティ要求
- **認証と認可:**
  - 参加者は、既存のチャットアプリを通じて認証し、イベントアプリへのアクセスを許可する。
- **データ保護:**
  - 写真データおよびスコアデータは暗号化して保存および転送する。
- **アクセス制御:**
  - 管理者と運営スタッフはそれぞれ異なるアクセス権限を持ち、不正アクセスを防ぐ。

#### 4. ユーザビリティ要求
- **ユーザーインターフェース:**
  - アプリは直感的で使いやすいインターフェースを提供し、ユーザーが迷わずに操作できるようにする。
- **ヘルプとサポート:**
  - アプリ内に詳細なヘルプセクションを用意し、参加者への迅速なサポートを提供。
- **多言語対応:**
  - 日本語と英語の2言語に対応し、国際的な参加者にも配慮する。

#### 5. 保守性要求
- **更新とアップグレード:**
  - イベント期間中も、中断なくアプリのアップデートやバグ修正が行える設計とする。
- **ログ管理:**
  - システムの全ての操作ログを記録し、トラブル発生時に迅速に問題を特定・解決できるようにする。
- **モジュール設計:**
  - アプリはモジュール化されており、個々の機能を独立して更新・修正できるようにする。

#### 6. 移植性要求
- **対応プラットフォーム:**
  - イベントアプリはiOSおよびAndroidの両方で利用可能とする。
- **ブラウザ互換性:**
  - 必要に応じて、主要なWebブラウザ（Chrome、Firefox、Safari）でも同様の機能が利用できるようにする。

#### 7. 信頼性要求
- **データの一貫性:**
  - データの一貫性を保ち、複数の参加者が同時に操作しても矛盾が生じないようにする。
- **障害回復:**
  - 障害発生時には迅速にデータの復旧を行い、参加者への影響を最小限に抑える。

#### 8. 法的および規制遵守要求
- **個人情報保護:**
  - 個人情報保護法に基づき、参加者の個人情報を適切に管理・保護する。
- **知的財産権:**
  - 写真データやその他のコンテンツについて、権利保護の観点から適切に処理する。

#### 9. 環境要求
- **適応性:**
  - アプリはキャンパス内のさまざまな場所で安定して動作すること。また、イベントの異なる季節や天候条件下でも利用できる。
- **インフラ対応:**
  - イベント会場のネットワーク環境に対応し、オフラインモードでも基本的な機能を利用できるようにする。

以上の非機能要求は、参加者のエンゲージメント向上やイベント運営の効率化を図るために重要な要素をカバーしています。これにより、イベントが成功するための技術的な基盤を強固にします。