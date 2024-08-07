# 機能要求書

## 1. 概要

本機能要求書は、キャンパス探索イベントに関連するシステムおよびアプリケーションの機能的な要求事項を定義する文書です。本システムの主な目標は、参加者がキャンパス内の指定ランドマークを探索し、楽しく学べる環境を提供することです。

## 2. 要件定義

### 2.1 イベントガイドの配布とアプリ起動

#### 2.1.1 イベントガイドの配布
- **機能**: イベント開始時に参加者へ物理的またはデジタル形式でイベントガイドを提供する。
    - **入力**: 参加者情報（氏名、連絡先など）
    - **出力**: イベントガイド（PDFまたは印刷物）
    - **インターフェース**: 物理配布またはメールによるデジタル配信

#### 2.1.2 QRコード提供とイベントアプリ起動
- **機能**: イベントガイドに含まれるQRコードをスキャンしてキャンパス探索イベントアプリを起動する。
    - **入力**: QRコードの読み取り
    - **出力**: イベントアプリの起動
    - **インターフェース**: モバイルデバイスのカメラおよび既存のチャットアプリ

### 2.2 ランドマークの探索

#### 2.2.1 ランドマークのリスト表示
- **機能**: キャンパス内の指定ランドマークのリストを参加者のアプリに表示する。
    - **入力**: ランドマーク情報（名称、位置、情報など）
    - **出力**: ランドマークリスト
    - **インターフェース**: イベントアプリのUI

#### 2.2.2 写真撮影とアップロード
- **機能**: 参加者がランドマークの写真を撮影し、アプリを通じてアップロードする。
    - **入力**: 撮影された写真
    - **出力**: クラウドサーバーへの写真のアップロード
    - **インターフェース**: モバイルデバイスのカメラおよびイベントアプリ

### 2.3 写真の自動解析とフィードバック

#### 2.3.1 写真の自動解析
- **機能**: アップロードされた写真を自動解析し、対応するランドマークを確認する。
    - **入力**: アップロードされた写真
    - **出力**: 解析結果（ランドマーク確認情報）
    - **インターフェース**: クラウド上の解析サーバー

#### 2.3.2 解説テキストとスコアの表示
- **機能**: 解析結果に基づいて関連する解説テキストやランドマークに関する情報、および探索のスコアをユーザに表示する。
    - **入力**: 解析結果、ランドマーク情報
    - **出力**: 解説テキスト、スコア
    - **インターフェース**: イベントアプリのUI

### 2.4 イベント終了と特典付与

#### 2.4.1 活動履歴の確認
- **機能**: イベント終了時に運営ステーションで参加者の活動履歴を確認する。
    - **入力**: 各参加者の活動履歴データ
    - **出力**: 活動履歴の要約
    - **インターフェース**: イベントアプリおよび管理用ダッシュボード

#### 2.4.2 特典の付与
- **機能**: 活動履歴と累積スコアに基づいて特典を付与する。
    - **入力**: 活動履歴、累積スコア
    - **出力**: 特典
    - **インターフェース**: 物理的またはデジタル特典配布システム

## 3. インターフェース要件

### 3.1 ユーザインターフェース
- **登録画面**: イベント登録およびQRコードスキャンのインターフェース
- **ランドマークリスト画面**: ランドマークの情報と位置を表示
- **カメラ画面**: 写真を撮影し、アップロードするインターフェース
- **解析結果画面**: 写真の解析結果、解説テキスト、スコアを表示

### 3.2 システムインターフェース
- **データベース**: ランドマーク情報、参照データの保存と取得
- **解析サーバー**: 写真の自動解析および結果の返送
- **管理ダッシュボード**: 活動履歴の確認と特典の管理

## 4. セキュリティ要件
- **認証**: QRコードを使用した参加者の認証
- **アクセス制御**: 役割に応じたアクセス権限の設定
- **暗号化**: データの保存および通信時の暗号化

## 5. パフォーマンス要件
- **応答時間**: 各操作における応答時間は1秒以内
- **データ処理速度**: 写真のアップロードと解析は5秒以内

## 6. 法令遵守
- **個人情報保護**: 個人情報保護法に準拠し、参加者データの適正な管理
- **ライセンス**: 使用するソフトウェアおよびシステムは関連するすべてのライセンスおよび規制を遵守

## 7. テストと監査

### 7.1 テスト要件
- **機能テスト**: 各機能が正しく動作するか確認
- **負荷テスト**: 予想される最大同時接続数の1.5倍の負荷テスト

### 7.2 監査要件
- **セキュリティ監査**: 年に一度の外部専門家によるセキュリティ監査

この機能要求書は、キャンパス探索イベントの成功と参加者の満足度向上を目指して設計されたシステムの機能要件を明確に定義することを目的としています。