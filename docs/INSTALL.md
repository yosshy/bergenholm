Installing Bergenholm
=====================

Install ISC DHCP server, TFTP server, MongoDB, iPXE, curl, pip and git. On Ubuntu 14.04, type a command below: 
```
$ sudo apt-get install isc-dhcp-server tftpd-hpa mongodb-server ipxe curl python-pip git
```
Ensure MongoDB server and TFTP daemon started.
```
$ sudo service mongodb restart
$ sudo service tftpd-hpa restart
```
Install Flask-PyMongo and Flask-Actions.
```
$ sudo pip install flask-pymongo flask-actions requests
```
Download Bergenholm.
```
$ git clone https://github.com/yosshy/bergenholm.git
```
Edit settings.py to modify MongoDB parameters. If you just installed mongodb-server, you don't have to modify them.
```
$ cd bergenholm
$ vi settings.py
```
Edit default parameters.
```
$ vi fixture/groups/default
```
Run Bergenholm.
```
$ sudo python manage.py runserver -p 80 &
```
Register fixtures.
```
$ cd fixture
$ sh register.sh
```
Test it. Say Bergenholm server's IP is 192.168.10.254.
```
$ curl http://127.0.0.1/hosts/
opc@ubuntu1404-x8664:~/bergenholm$ curl http://127.0.0.1/api/1.0/hosts/
{
  "hosts": [
    "samplehost",
    "default",
    "register",
  ]
}
$ curl -v http://127.0.0.1/groups/
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
$ curl http://127.0.0.1/templates/
{
  "templates": [
    "linux.ipxe",
    "ubuntu1404.preseed",
    "centos6.kickstart"
  ]
}
$ curl http://127.0.0.1/hosts/samplehost
{
  "groups": [
    "centos6",
    "centos.amd64"
  ],
  "hostname": "test-200",
  "ipaddr": "192.168.10.200"
}
$ curl http://127.0.0.1/hosts/samplehost?params=all
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
Edit /etc/dhcp/dhcpd.conf. bergenholm/examples/dhcpd.conf helps you.

Copy undionly.kpxe to TFTP root directory.
```
$ sudo cp /usr/lib/ipxe/undionly.kpxe /var/lib/tftpboot/
```
Restart dhcpd.
```
$ sudo service isc-dhcp-server restart
```
