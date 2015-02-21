# Bergenholm

Bergenholm (バーゲンホルム) は Cobbler や MAAS のような、シンプルなキッ
クスタートインストールサーバです。

## 特長

* iPXE 活用：iPXE は x86/x86-64 用ネットワークブートローダです。iPXE は
  多数の機能を持っており、中でも HTTP ダウンロード、独自のスクリプト言
  語、ホスト依存パラメータ等の機能を Bergenholm は使用しています。

* ローカルリポジトリ無し：Cobbler や MAAS には、それらが管理するインス
  トール用のローカルリポジトリがありますが、Bergenholm にはローカルリポ
  ジトリが必要ありません。勿論、手動でローカルリポジトリを作成し、
  Bergenholm にそれを利用させる事も出来ます。

* REST API：Bergenholm は、テンプレート用、ホスト用、グループ用、iPXE
  用の各 RESTful API を持っています。GUI/WebUI は今のところありません。

* パラメータ継承：Bergenholm はホストとグループで JSON 型のパラメータを
  扱います。ホストパラメータはグループのパラメータを(多重)継承する事が
  でき、グループも別のグループのパラメータを継承する事ができます。グルー
  プ定義について特別な制限はありません。

* Jinja2 テンプレート：Bergenholm は Jinja2 形式のテンプレートファイル
  とパラメータを扱う事ができます。Kickstart や Preseed ファイル用途で、
  テンプレートファイルはホストやグループのパラメータを使用する事ができ
  ます。予約パラメータを除き、パラメータ定義に制約はありません。

* リモートファイルのストリーミング：Bergenholm はリモートサイト上のカー
  ネルや initrd イメージを取得し、インストール先サーバに対してそのファ
  イルを転送（ストリーミング）する事ができます。

* Flask-PyMongo/Flask-Action ベース：バックエンド DB は MongoDB です。
  また、Python で Bergenholm を開発する事ができます。


## 構造

![Figure: Structure]
(https://github.com/yosshy/bergenholm/raw/master/docs/structure.png)


## 起動シーケンス

(IT=インストール先サーバ, KS=キックスタートインストールサーバ)

共通部分：

1. IT: 電源ON (電源ボタン、IPMI、他)
2. IT: DHCP 要求送信 (NIC BIOS)
3. KS: 次のダウンロードファイル情報を含む DHCP 応答送信 (DHCP サーバ)
4. IT: 次のダウンロードファイル (iPXE) 取得の TFTP 要求送信 (NIC BIOS)
5. KS: iPXE イメージを TFTP 経由で送信 (TFTP サーバ)
6. IT: iPXE 用スクリプト取得の HTTP 要求送信 (iPXE)
7. KS: iPXE 用スクリプトを HTTP 経由で送信 (Bergenholm)

ケース・バイ・ケース部分：

(ネットワークインストール)

8. IT: 起動イメージ(カーネル、initrd 等)取得の HTTP 要求送信(iPXE)
9. KS: リモートイメージを (Web プロキシ経由で) 取得 (Bergenholm)
10. KS: HTTP 経由で起動イメージを IT に送信 (Bergenholm)

(ローカルブート)

8. IT: ローカルストレージから起動 (iPXE)

(IT 登録)

8.  IT: IT 自体を Bergenholm に登録する為の HTTP 要求送信 (iPXE)
9.  KS: IT を DB 登録 (Bergenholm)
10. IT: ローカルストレージから起動 (iPXE)


## インストール

[INSTALL.ja.md]
(https://github.com/yosshy/bergenholm/blob/master/docs/INSTALL.ja.md)
を参照して下さい。


## 使用法

[USAGE.ja.md]
(https://github.com/yosshy/bergenholm/blob/master/docs/USAGE.ja.md) 
を参照して下さい。bergenholmclient をインストールしている場合は、
[USAGE_CLI.ja.md]
(https://github.com/yosshy/bergenholm/blob/master/docs/USAGE_CLI.ja.md)
の方が良いでしょう。


## クライアント

* [コマンドラインツール](https://github.com/yosshy/bergenholmclient)


## API

[API.ja.md]
(https://github.com/yosshy/bergenholm/blob/master/docs/API.ja.md) 
を参照して下さい。


## よくある質問

[FAQ.ja.md]
(https://github.com/yosshy/bergenholm/blob/master/docs/FAQ.ja.md) 
を参照して下さい。


## 注記

* ubuntu1404.preseed は
  https://github.com/wnoguchi/ubuntu_documents/tree/master/preseed をベー
  スにしています。
* centos6.kickstart は https://github.com/CentOS/Community-Kickstarts
  をベースにしています。


## 再配布ライセンス

Bergenholm の再配布ライセンスは Apache License ver.2.0 です。LICENSE を
参照して下さい。

注意：centos6.kickstart は GNU GPL ver.2 です。ubuntu1404.preseed のオ
リジナルは再配布ライセンス表記がありあせん。
