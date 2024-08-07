### 非機能要求書

#### 1. 導入とスコープ

本非機能要求書は、イベント参加者がキャンパス内の指定ランドマークを探索し、写真を撮影・アップロードするイベントに関連するシステムの非機能要件を定義します。本要件は、システムのパフォーマンス、信頼性、可用性、保守性、セキュリティなどを含む。

---

#### 2. パフォーマンス要件

1. **応答時間**
   - イベントアプリの画面切り替えやデータ表示の応答時間は1秒以内とする。
   - QRコード読み取り後、アプリが起動するまでの時間は3秒以内とする。

2. **データ処理速度**
   - 写真のアップロードと解析に要する時間は5秒以内とする。
   - 写真解析後の関連解説テキストやスコア表示は1秒以内とする。

---

#### 3. 信頼性要件

1. **稼働時間**
   - イベント開催期間中、システムの稼働率は99.9%以上とする。
   - ダウンタイムは許容されない。

2. **エラー処理**
   - QRコード読み取りや写真アップロード時にエラーが発生した場合、ユーザに対して適切なエラーメッセージを表示し、再試行を可能にする。

---

#### 4. 可用性要件

1. **サービス継続**
   - 参加者がイベント中にアプリを常時使用できる状態を維持するため、システムの負荷分散とフェールオーバー機能を実装する。
   - ネットワーク障害時にもオフラインでの基本機能を提供する。

---

#### 5. 保守性要件

1. **システムアップデート**
   - 定期的なシステムアップデートを行い、非イベント期間中のメンテナンス時間を確保する。
   - 問題発生時には迅速に対応できる保守チームを配置する。

2. **ログとモニタリング**
   - システムのパフォーマンスとエラーを監視するためのロギング機能を提供する。
   - 重要なイベントやエラー発生時には自動通知を行う。

---

#### 6. セキュリティ要件

1. **データ保護**
   - 写真データやスコアデータは暗号化して保存する。
   - 通信経路上の全てのデータはSSL/TLSで暗号化する。

2. **アクセス制御**
   - 参加者、運営スタッフ、システム管理者それぞれに対するアクセス権限を最低限の範囲で設定する。

3. **ユーザ認証**
   - QRコードを利用したイベントアプリ起動時に、参加者の認証を行う。
   - 管理者は二要素認証によるアクセスを実施する。

---

#### 7. 性能テストと監査

1. **負荷テスト**
   - 予想される最大同時接続数の1.5倍をターゲットに負荷テストを実施し、システムの耐久性を確認する。

2. **セキュリティ監査**
   - 年に一度、外部のセキュリティ専門家によるセキュリティ監査を実施すること。

---

#### 8. 法令遵守

1. **個人情報保護**
   - 個人情報保護法に準拠し、参加者のデータを適正に管理・保護する。

2. **ライセンスと規制**
   - 使用するソフトウェアおよびシステムは、関連する全てのライセンスおよび規制を遵守すること。

---

この非機能要求書は、イベントの成功と参加者の満足度向上を目指し、適切なシステムの設計・運用を支援することを目的としています。これにより、イベントの円滑な進行とリスクの低減を実現します。