以下に機能要求書を作成しました。非機能要求書の内容を基にし、具体的なユーザー操作やシステムの動作を明記しています。

### 機能要求書 (FR)

#### システム名称
キャンパス探索イベントアプリ

---

#### 機能要求一覧

##### 1. 認証およびユーザー管理機能
1.1 **ユーザー認証**
- 参加者は既存のチャットアプリ（例：LINE、WeChat）を通じて認証を行います。
- 認証後、初回ログイン時にプロフィール情報（名前、メールアドレス等）を入力する。

1.2 **ユーザー役割管理**
- 役割ごとに異なるアクセス権限を設定します。
  - 参加者: イベント内容の確認、写真のアップロード、スコアの確認。
  - 運営スタッフ: 参加者の管理、イベントの進行管理。
  - 管理者: システム設定、全データへのアクセス。

##### 2. イベント管理機能
2.1 **イベント情報の表示**
- イベントの日時、場所、詳細情報を参加者に表示します。
- 地図機能を用いてイベント会場の位置を示します。

2.2 **リアルタイム更新**
- イベント情報が変更された場合、参加者へプッシュ通知を送信します。

##### 3. 写真アップロードおよび解析機能
3.1 **写真のアップロード**
- 参加者はイベント中に写真をアップロードできる。
- アップロードされた写真は自動的にサーバーに送信され、バックグラウンドで解析が行われる。

3.2 **自動解析とスコアリング**
- 写真の内容を自動解析し、10秒以内にスコアを算出する。
- 分析結果（スコア、解析内容）を参加者に通知します。

##### 4. スコア管理機能
4.1 **スコアの表示**
- イベント参加者の個別スコアおよび順位をリアルタイムで表示します。
- 総合スコアや獲得バッジなどの情報も併せて表示する。

4.2 **リーダーボード**
- スコアに基づき、参加者のランキングを表示します。
- 上位者には特別なバッジや称号を自動付与。

##### 5. チャット機能
5.1 **インタラクティブチャット**
- 参加者と運営スタッフ間での連絡を円滑にするため、チャット機能を提供します。
- メッセージの送信、受信をリアルタイムで行う。

5.2 **グループチャット**
- 特定のイベントに関連するグループチャットに参加可能。
- グループメンバーと情報共有やディスカッションを行う。

##### 6. フィードバック機能
6.1 **リアルタイムフィードバック収集**
- 参加者からリアルタイムでフィードバックを収集し、運営側に通知。
- フィードバックはカテゴリ（例：バグ報告、改善提案、感想）ごとに整理される。

6.2 **フィードバックの反映**
- 収集したフィードバックをイベント中に迅速に反映するための審査機能を提供。

##### 7. アドミン機能
7.1 **イベント設定管理**
- 管理者は新規イベントの作成、既存イベントの編集、削除を行うことができる。
- 各イベントの詳細情報（日時、場所、参加条件など）を設定可能。

7.2 **ユーザー管理**
- 全ユーザーのアカウント情報、参加履歴、スコア履歴を閲覧・管理。
- 不正行為が発覚した場合のアカウント停止機能を提供。

##### 8. レポーティング機能
8.1 **参加者データのエクスポート**
- イベント終了後、参加者データをCSV形式でエクスポートする機能を提供。
- データには、参加者のプロフィール情報、スコア、フィードバックが含まれる。

8.2 **レポート生成**
- イベントの成果をまとめた自動レポートを生成。
- レポートはPDF形式で出力でき、イベントを振り返るための資料として利用可能。

#### 最後に

この機能要求書は、キャンパス探索イベントのスムーズな運営と参加者のエンゲージメント向上を目指し、ユーザビリティ、セキュリティ、パフォーマンスを高めることを目的としています。全ての機能がステークホルダーの期待とプロジェクト成功基準を満たすように設計されています。今後のシステム開発において、これらの要求を遵守し、最高のユーザー体験を提供することを確約いたします。