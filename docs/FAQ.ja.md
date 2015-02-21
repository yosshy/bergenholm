# Bergenholm: よくある質問


## Bergenholm って何？

Bergenholm は以下と同様のキックスタートインストールです。

* [Cobbler](http://www.cobblerd.org/)
* [MAAS](https://maas.ubuntu.com/)

## Bergenholm の特長は？

Bergenholm はシンプルで小さなプログラムですが、以下の特長があります。

* REST API のみ
* [iPXE](http://ipxe.org/) を効果的に使用
* ローカルリポジトリ無し
* グループからのパラメータ継承
* Jinja2 テンプレート（iPXE スクリプト、kickstart/pressed ファイル、あ
  るは他の用途)
* (Web プロキシ経由の) リモートファイル転送
* Flask-PyMongo/Flask-Actions で開発

## 何故 Bergenholm を作ったの？

* ローカルリポジトリは、大量のサーバへのインストールでは有用ですが、１～
  数台のインストールでは必要ありません。このようなケースでは、必ずロー
  カルリポジトリを作成する MAAS や Cobbler は適していません。
  Bergenholm はローカルリポジトリを必要としませんが、既存のローカルリポ
  ジトリを使うように設定する事もできます。

* MAAS や Cobbler は複雑で開発に不向きです。Bergenholm は Flask ベース
  なので、内容を学習して改造するのも簡単です。

* iPXE は新しくて優れたネットワークブートローダです(特に HTTP 経由での
  イメージ取得機能)。しかし、iPXE を有効活用したソフトウェアはありませ
  ん。Bergenholm は iPXE を有効活用した最初のソフトウェアかも知れません。

* Cobbler は distros, profiles, sub-profiles, systems, images, repos パ
  ラメータクラスを扱い、これらの間でパラメータを継承する事ができます。
  しかし、これらは複雑で柔軟性がなく、多重継承ができません。Bergenholm
  は host と group の２つのパラメータクラスしかありません。host と
  group は、内部の groups パラメータで指定された他のグループのパラメー
  タを継承できます。ご想像通り、groups は group 名のリストです。

* Cobbler と MAAS は、それらが管理する DHCP サービス(と DNS サービス)の
  為に HA クラスタの構築が難しいです。Bergenholm は単なる Web アプリケー
  ションであり、DHCP 設定を管理しません。よって、Bergenholm は簡単に冗
  長／負荷分散クラスタ化できます。

## 何故 Bergenholm という名前にしたの？

「バーゲンホルム機関 (Bergenholm space drive)」はレンズマンシリーズに登
場する超光速移動技術の名称です。
http://en.wikipedia.org/wiki/Bergenholm_space_drive

名前を決めるにあたって、以下の条件で選びました。

* Ansible のような超光速技術の名称
* 既存ソフトウェア (特に OSS) で同じ名前のものがない
* <名前>.com が使われていない

## 認証は？

Apache HTTP サーバか Nginx 経由で使って下さい。

## ローカルリポジトリと組み合わせるには？

linux.ipxe を修正するか、新しい .ipxe テンプレートを登録して下さい。
内容は以下の様なものです。

<pre>
#!ipxe
kernel {{repos_url}}/path/to/vmlinuz ks=...
module {{repos_url}}/path/to/initrd
boot
</pre>

新しい .ipxe テンプレートを登録した場合、host/group パラメータクラスで
そのテンプレートを指定する必要があります。
