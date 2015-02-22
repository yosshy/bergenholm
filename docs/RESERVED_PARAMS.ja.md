# Bergenholm: 予約パラメータ

## proxy_url

HTTP プロキシのURL。設定された場合、Bergenholm は kernel/moudle イメー
ジのダウンロード proxy_url で指定された HTTP プロキシを使用します。

## ipxe_script

iPXE スクリプトのテンプレート名。"```GET /ipxe/scrit/<uuid>```" 要求時、
Bergenholm は ipxe_script パラメータで指定されたテンプレートを uuid で
指定されたホストパラメータでレンダリングした結果を送付します。

## kernel

リモートサイト上のカーネルイメージの URL。"```GET
/ipxe/kernel/<uuid>```" 要求時、Bergenholm は kernel パラメータをカーネ
ルのダウンロード元として使用します。

## module

リモートサイト上のモジュール(initrd)の URL。以下要求時、Bergenholm は
module パラメータをモジュールのダウンロード元として使用します。

* ```GET /ipxe/module/<uuid>```
* ```GET /ipxe/module/<uuid>/0```
* ```GET /ipxe/initrd/<uuid>```
* ```GET /ipxe/initrd/<uuid>/0```

## moduleN (N=0〜、整数)

リモートサイト上のモジュール(initrd)の URL。以下要求時、Bergenholm は
moduleN パラメータをモジュールのダウンロード元として使用します。

* ```GET /ipxe/module/<uuid>/<N>```
* ```GET /ipxe/initrd/<uuid>/<N>```
