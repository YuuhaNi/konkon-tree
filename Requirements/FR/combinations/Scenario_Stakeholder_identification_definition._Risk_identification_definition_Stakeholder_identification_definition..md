### 機能要求書

#### 1. 導入とスコープ

本機能要求書は、イベント参加者がキャンパス内の指定ランドマークを探索し、写真を撮影・アップロードするイベントに関連するシステムの機能要件を定義するものです。本システムは参加者の体験を向上させ、イベントの円滑な運営を支援することを目的としています。以下に、本システムが提供する具体的な機能要件を示します。

---

#### 2. コア機能

2.1 イベント登録・ログイン機能
- **機能:** 参加者は専用のQRコードや招待リンクを使用してイベントに登録し、ログインすることができる。
- **理由:** 参加者の認証と統計データのトラッキングのため。

2.2 ランドマーク探索機能
- **機能:** 参加者はイベントアプリを通して指定されたランドマークのリストを表示し、各ランドマークの位置情報や詳細情報を確認することができる。
- **理由:** 参加者の利便性向上とイベントの進行を円滑にするため。

2.3 写真撮影・アップロード機能
- **機能:** 参加者はランドマークで写真を撮影し、アプリを通じて即座にアップロードできる。アップロードされた写真はサーバで保存され、解析される。
- **理由:** イベントのテーマに基づいた参加者の活動を収集するため。

2.4 写真解析とスコアリング機能
- **機能:** システムはアップロードされた写真を解析し、撮影されたランドマークが正しいかを確認する。また、正確な写真に基づいてスコアを自動的に計算し、リアルタイムで参加者にフィードバックする。
- **理由:** 参加者のパフォーマンスを評価し、イベントの競争性を高めるため。

2.5 スコアボード機能
- **機能:** 参加者のスコアをリアルタイムで集計し、ランキング形式で表示する。スコアボードはアプリ内でいつでも確認できる。
- **理由:** 参加者のモチベーションを維持し、競争を促すため。

---

#### 3. ナビゲーション機能

3.1 マップ表示機能
- **機能:** 指定されたランドマークの位置を地図上に表示し、ナビゲーションを提供する。参加者はリアルタイムで自分の位置を確認できる。
- **理由:** 参加者が効率的にランドマークを探索できるようにするため。

3.2 ナビゲーションガイド機能
- **機能:** 目的地までのルートおよびターンバイターンのガイドを提供する。また、音声ガイドもオプションで利用できる。
- **理由:** 道案内の精度向上とユーザビリティの向上を図るため。

---

#### 4. ソーシャル機能

4.1 チャット機能
- **機能:** 参加者間でリアルタイムチャットができる機能を提供する。イベント運営者からのお知らせや緊急連絡もチャットを通じて行う。
- **理由:** 参加者同士のコミュニケーションおよび運営者との連携を円滑にするため。

4.2 フォトギャラリー機能
- **機能:** 参加者がアップロードした写真をギャラリー形式で閲覧できる。また、他の参加者の写真に対して「いいね」やコメントを残す機能も含む。
- **理由:** 参加者の活動を共有し、イベントの一体感を醸成するため。

---

#### 5. 管理機能

5.1 ユーザ管理機能
- **機能:** イベント運営者が参加者の登録情報やスコアを管理・編集できる機能を提供する。また、不正な活動を行うユーザーのアクセスを制限する機能も含む。
- **理由:** イベントの円滑な運営と透明性の確保のため。

5.2 ランドマーク管理機能
- **機能:** イベント開催前にランドマークの設定や変更ができる機能を提供する。ランドマークの追加や削除、位置情報の更新を含む。
- **理由:** フレキシブルなイベント運営ができるようにするため。

5.3 レポート生成機能
- **機能:** イベント終了後、参加者の活動データ、スコア、利用状況などの詳細レポートを自動生成する機能を提供する。
- **理由:** イベントの成果を評価し、次回以降のイベントの改善に役立てるため。

---

#### 6. セキュリティ機能

6.1 データ暗号化機能
- **機能:** すべての参加者データ、写真データ、通信データを暗号化し、データ保護を強化する。
- **理由:** 参加者の個人情報とデータ保護のため。

6.2 多要素認証機能
- **機能:** 管理者アカウントに対する多要素認証を実装し、不正アクセスを防止する。
- **理由:** システムのセキュリティを強化し、権限管理を厳密に行うため。

---

この機能要求書は、本イベントの成功と参加者の満足度向上を目的としており、イベントのスムーズな進行とリスクの低減を実現するために策定されました。