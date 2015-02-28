# Bergenholm: 予約パラメータ

## proxy_url

HTTP プロキシのURL。設定された場合、Bergenholm は kernel/moudle イメー
ジのダウンロード proxy_url で指定された HTTP プロキシを使用します。

## ipxe_script

iPXE スクリプトのテンプレート名。"`GET /ipxe/scrit/<uuid>`" 要求時、
Bergenholm は ipxe_script パラメータで指定されたテンプレートを uuid で
指定されたホストパラメータでレンダリングした結果を送付します。

## kernel

リモートサイト上のカーネルイメージの URL。"`GET
/ipxe/kernel/<uuid>`" 要求時、Bergenholm は kernel パラメータをカーネ
ルのダウンロード元として使用します。

## module

リモートサイト上のモジュール(initrd)の URL。以下要求時、Bergenholm は
module パラメータをモジュールのダウンロード元として使用します。

* `GET /ipxe/module/<uuid>`
* `GET /ipxe/module/<uuid>/0`
* `GET /ipxe/initrd/<uuid>`
* `GET /ipxe/initrd/<uuid>/0`

## moduleN (N=0〜、整数)

リモートサイト上のモジュール(initrd)の URL。以下要求時、Bergenholm は
moduleN パラメータをモジュールのダウンロード元として使用します。

* `GET /ipxe/module/<uuid>/<N>`
* `GET /ipxe/initrd/<uuid>/<N>`

## power_driver

Power API で使用される電源管理ドライバ名。"vmware", "ipmi", "dummy" の
いずれかを指定します。

## vmware_host
## vmware_port
## vmware_user
## vmware_password

power_driver が "vmware" の場合に使用される、VMware API のそれぞれホス
ト名（又は IP アドレス）、ポート番号、ユーザ名、パスワードです。

## ipmi_host
## ipmi_port
## ipmi_user
## ipmi_password

power_driver が "ipmi" の場合に使用される、IPMI LAN I/F のそれぞれホス
ト名（又は IP アドレス）、ポート番号、ユーザ名、パスワードです。

## libvirt_url

power_driver が "libvirt" の場合に使用される、Libvirtd への接続 URL で
す。
