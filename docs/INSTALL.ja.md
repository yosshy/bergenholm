# Bergenholm のインストール


ISC DHCP サーバ、TFTP サーバ、MongoDB、iPXE、curl、pip、git をインストールします。
Ubuntu 14.04 では以下のコマンドを実行して下さい。
```
$ sudo apt-get install isc-dhcp-server tftpd-hpa mongodb-server ipxe curl python-pip git
```
MongoDB サーバと TFTP デーモンが起動している事を確認して下さい。
```
$ sudo service mongodb restart
$ sudo service tftpd-hpa restart
```
Flask-PyMongo、Flask-Action をインストールします。
```
$ sudo pip install flask-pymongo flask-actions requests Werkzeug==0.9.4
```
電源管理ドライバ用の Python モジュールをインストールします。
```
$ sudo apt-get install python-pyghmi python-libvirt
$ sudo pip install pyvmomi
```
Bergenholm をダウンロードします。
```
$ git clone https://github.com/yosshy/bergenholm.git
```
settings.py 上の MongoDB 関連パラメータを編集します。mongodb-server をインストールした直後であれば、修正する必要はありません。
```
$ cd bergenholm
$ vi settings.py
```
デフォルトのパラメータを編集します。
```
$ vi fixture/groups/default
```
Bergenholm を起動します。
```
$ sudo python manage.py runserver -p 80 &
```
サンプルデータを登録します。
```
$ cd fixture
$ ./register.sh
```
テストします。Bergenholm サーバの IP アドレスを 192.168.10.254 とすると、
```
$ curl http://127.0.0.1/api/1.0/hosts/
{
  "hosts": [
    "samplehost",
    "default",
    "register",
  ]
}
$ curl -v http://127.0.0.1/api/1.0/groups/
{
  "groups": [
    "default",
    "ubuntu1204",
    "ubuntu",
    "ubuntu1404",
    "ubuntu1410",
    "centos6",
    "centos",
    "centos.amd64",
    "centos.x86",
    "ubuntu.amd64",
    "ubuntu.x86"
  ]
}
$ curl http://127.0.0.1/api/1.0/templates/
{
  "templates": [
    "linux.ipxe",
    "ubuntu1404.preseed",
    "centos6.kickstart"
  ]
}
$ curl http://127.0.0.1/api/1.0/hosts/samplehost
{
  "groups": [
    "centos6",
    "centos.amd64"
  ],
  "hostname": "test-200",
  "ipaddr": "192.168.10.200"
}
$ curl http://127.0.0.1/api/1.0/hosts/samplehost?params=all
{
  "arch": "x86_64",
  "base_url": "http://192.168.10.254",
  "gateway": "192.168.10.254",
  "groups": [
    "centos6",
    "centos.amd64"
  ],
  "hostname": "test-200",
  "image_base_url": "http://mirror.centos.org/centos-6/6/os/x86_64/images/pxeboot",
  "ipaddr": "192.168.10.200",
  "ipxe_script": "linux.ipxe",
  "ipxe_url": "http://192.168.10.254/ipxe",
  "kernel": "http://mirror.centos.org/centos-6/6/os/x86_64/images/pxeboot/vmlinuz",
  "kernel_opts": "ks=http://192.168.10.254/templates/centos6.kickstart/${uuid}",
  "kickstart": "centos6.kickstart",
  "mirror_url": "http://mirror.centos.org/centos-6/6/os/x86_64",
  "module": "http://mirror.centos.org/centos-6/6/os/x86_64/images/pxeboot/initrd.img",
  "nameserver": "192.168.0.254",
  "netmask": "255.255.255.0",
  "proxy_url": "http://proxy.example.com:8080",
  "version": "6"
}
```
/etc/dhcp/dhcpd.conf を編集します。bergenholm/examples/dhcpd.conf が参考になるでしょう。

また、dhcpd が使用するネットワークデバイスを指定する為、/etc/default/isc-dhcp-server を編集する必要があるかも知れません。

undionly.kpxe を TFTP のルートディレクトリにコピーします。
```
$ sudo cp /usr/lib/ipxe/undionly.kpxe /var/lib/tftpboot/
```
dhcpd を再起動します。
```
$ sudo service isc-dhcp-server restart
```
