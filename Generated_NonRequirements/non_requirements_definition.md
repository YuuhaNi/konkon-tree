## 1. 運用環境

### 1.1 リモートオペレーション
- **概要:** 運営スタッフがリモートでシステムのモニタリングとサポートを可能にする。
- **要件:** インターネット接続が必要なため、セキュアな遠隔アクセス環境を提供する。

### 1.2 外部システム接続
- **概要:** 他の既存システムやデバイスと連携する必要がある。
- **要件:** チャットアプリとのシームレスな統合が必要で、インターフェース/APIが確保されるべき。

### 1.3 サポート体制
#### 1.3.1 サポート要員
- **概要:** 運営ステーションにて運営スタッフが常駐。
- **要件:** 運営スタッフはアプリケーションの一次対応を行うため、基本的なトレーニングが必要。

## 2. 可用性

### 2.1 継続性
#### 2.1.1 運用スケジュール
- **概要:** アプリケーションが常時利用可能であること。
- **要件:** オープンキャンパスの開催期間中は24時間稼働すること。

#### 2.1.2 計画停止の有無
- **概要:** メンテナンスのために予定している停止時間。
- **要件:** 最小化し、事前に参加者に通知する。

#### 2.1.3 業務継続性
- **概要:** イベント開催中にサービスが中断しないようにするための対策。
- **要件:** 定期的なバックアップとフェールオーバープロセスを設定する。

#### 2.1.4 対象業務範囲
- **概要:** システムがカバーする業務範囲。
- **要件:** 参加者のアクティビティとスコア管理、スタッフのモニタリング機能を含む。

#### 2.1.5 サービス切替時間
- **概要:** フェールオーバー時の切替に要する時間。
- **要件:** 5分以内にサービスを再開できること。

#### 2.1.6 業務継続の要求度
- **概要:** サービス停止による影響度。
- **要件:** イベント開催時は100%稼働を目指す。

#### 2.1.7 RPO（目標復旧地点）
- **概要:** データ復旧を行う際の許容される最新の時点。
- **要件:** 最大でも5分前のデータが復旧可能であること。

#### 2.1.8 RTO（目標復旧時間）
- **概要:** サービス停止から再開までの最大許容時間。
- **要件:** 最大10分以内に復旧可能であること。

#### 2.1.9 RLO（目標復旧レベル）
- **概要:** サービス再開時の機能レベル。
- **要件:** 基本機能（写真アップロード、スコア表示）の最低限のサービスが提供される。

#### 2.1.10 目標復旧水準（大規模災害時）
- **概要:** 大規模災害が発生した場合の復旧水準。
- **要件:** 重要データのバックアップが遠隔地に保管されており、72時間以内に完全復旧が可能。

### 2.2 稼働率
#### 2.2.1 稼働率
- **概要:** システムの利用可能時間の割合。
- **要件:** 99.9%以上の稼働率を維持すること。

## 3. 耐障害性

### 3.1 サーバ
#### 3.1.1 冗長化（機器）
- **概要:** サーバ機器の冗長化。
- **要件:** 2重化し、フェールオーバー可能な構成を用いる。

#### 3.1.2 冗長化（コンポーネント）
- **概要:** サーバ内の重要コンポーネントの冗長化。
- **要件:** 電源、ネットワークカード、ストレージなどの冗長化。

### 3.2 端末
#### 3.2.1 冗長化（機器）
- **概要:** 参加者端末の冗長化。
- **要件:** 予備の端末を運営ステーションに配置。

#### 3.2.2 冗長化（コンポーネント）
- **概要:** 参加者端末の部品冗長化。
- **要件:** バッテリーや充電器などの消耗品を充分に用意しておく。

### 3.3 ネットワーク機器
#### 3.3.1 冗長化（機器）
- **概要:** ネットワーク機器の冗長化。
- **要件:** 主要ネットワーク機器の二重化。

#### 3.3.2 冗長化（コンポーネント）
- **概要:** ネットワーク機器内部の冗長化。
- **要件:** インタフェースや電源の冗長化。

### 3.4 ネットワーク
#### 3.4.1 回線の冗長化
- **概要:** ネットワーク回線の予備を確保。
- **要件:** 複数ISPを使用し、回線障害に備える。

#### 3.4.2 経路の冗長化
- **概要:** 複数経路の設定。
- **要件:** ルーティングプロトコルの適用による経路の自動切替。

#### 3.4.3 セグメント分割
- **概要:** ネットワーク内のセグメント分割。
- **要件:** イベントアプリ用とその他サービス用を分離し、影響を限定化する。

### 3.5 ストレージ
#### 3.5.1 冗長化（機器）
- **概要:** ストレージ機器の冗長化。
- **要件:** RAID構成やクラウドストレージを使用。

#### 3.5.2 冗長化（コンポーネント）
- **概要:** ストレージコンポーネントの冗長化。
- **要件:** 複数のディスクやコントローラの冗長化。

#### 3.5.3 冗長化（ディスク）
- **概要:** ディスクの冗長化。
- **要件:** RAIDによる冗長化を行う。

### 3.6 データ
#### 3.6.1 バックアップ方式
- **概要:** データのバックアップ方法。
- **要件:** リアルタイムのデータミラーリングと定期的なスナップショット。

#### 3.6.2 データ復旧範囲
- **概要:** 復旧可能なデータ範囲。
- **要件:** 全データの完全復旧が可能であること。

#### 3.6.3 データインテグリティ
- **概要:** データの完全性。
- **要件:** チェックサムやハッシュを利用し、データの整合性を保証。

## 4. セキュリティ

### 4.1 不正追跡・監視
#### 4.1.1 不正監視
- **概要:** 不正アクセスや操作を監視するシステム。
- **要件:** リアルタイムのログ監視とアラートシステムを導入。

#### 4.1.2 データ検証
- **概要:** データの正当性を検証。
- **要件:** 定期的なデータ検証と監査を行う。

### 4.2 ネットワーク対策
#### 4.2.1 マルウェア対策
- **概要:** マルウェアからシステムを守る対策。
- **要件:** アンチウイルスソフトウェアと侵入検知システムを使用。

#### 4.2.2 リアルタイムスキャンの実施
- **概要:** リアルタイムでの感染検知。
- **要件:** 継続的なスキャンとアップデートを適用。

### 4.3 セキュリティリスク管理
#### 4.3.1 セキュリティパッチ適用
- **概要:** ソフトウェアの最新パッチを常に適用。
- **要件:** 定期的なパッチマネジメント。

#### 4.3.2 アクセス・利用制限
- **概要:** システムの利用制限。
- **要件:** 役割に応じたアクセス制御を導入。

#### 4.3.3 データ暗号化
- **概要:** データを保護するために暗号化。
- **要件:** 重要データはすべて暗号化。

### 4.4 セキュリティ診断
#### 4.4.1 セキュリティ診断
- **概要:** 定期的なシステムの脆弱性診断。
- **要件:** 外部専門機関による定期的な診断。

### 4.5 セキュリティリスク管理
#### 4.5.1 セキュリティリスクの見直し
- **概要:** セキュリティリスクの定期的な見直し。
- **要件:** 半年ごとにリスクアセスメントを実施。

#### 4.5.2 リスク対策方針
- **概要:** リスクに対する対策の方針。
- **要件:** 対策プランの策定と実施。

## 5. 性能・拡張性

### 5.1 業務処理量
#### 5.1.1 通常時の業務量
- **概要:** 通常時のシステム負荷。
- **要件:** 最大同時接続数500名に耐えうる性能。

#### 5.1.2 業務量増大度
- **概要:** 業務量の変動に対する対応能力。
- **要件:** 50%増のアクセスが発生しても影響がないこと。

### 5.2 保管期間
- **概要:** データの保管期間。
- **要件:** 少なくともイベント終了後1年間のデータ保管。

### 5.3 性能目標値
#### 5.3.1 オンラインレスポンス
- **概要:** システムの応答時間。
- **要件:** アクセスから操作完了までの応答時間が2秒以内。

### 5.4 リソース拡張性
#### 5.4.1 CPU拡張性
- **概要:** CPUリソースの拡張性能。
- **要件:** 必要に応じて追加可能なCPUスロットを持つ。

#### 5.4.2 メモリ拡張性
- **概要:** メモリリソースの拡張性能。
- **要件:** 必要に応じて追加可能なメモリスロットを持つ。

### 5.5 帳票印刷能力
#### 5.5.1 帳票印刷に要求されるスループット
- **概要:** 印刷のための処理能力。
- **要件:** 1時間あたり100ページの印刷能力。

## 6. 運用・保守性

### 6.1 通常運用
#### 6.1.1 バックアップ
- **概要:** データの定期バックアップ。
- **要件:** デイリーバックアップとリアルタイムミラーリング。

### 6.2 保守運用
#### 6.2.1 計画停止
- **概要:** 計画的なシステム停止によるメンテナンス。
- **要件:** 予告と同意を得た上で、オフピーク時に実施。

#### 6.2.2 予防保守レベル
- **概要:** 予防保守の程度。
- **要件:** システム部品の定期点検と交換。

#### 6.2.3 保守作業自動化の範囲
- **概要:** 保守業務の自動化。
- **要件:** バックアップやログ収集を自動化。

### 6.3 障害時運用
#### 6.3.1 復旧作業
- **概要:** システム障害時の復旧作業。
- **要件:** 対応マニュアルの整備と復旧訓練。

#### 6.3.2 システム異常検知時の対応
- **概要:** 異常を検知した際の対応手順。
- **要件:** 自動アラートと対応手順の確立。

#### 6.3.3 交換用部材の確保
- **概要:** 交換部材の確保。
- **要件:** 主要部材の予備を確保し、即時交換可能にする。