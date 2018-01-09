# Bergenholm

Bergenholm is a simple kickstart install server like Cobbler or MAAS.

Japanese version of this document is
[README.ja.md](https://github.com/yosshy/bergenholm/blob/master/README.ja.md).

## Features

* Using iPXE efficiently; iPXE is a PXE boot loader for x86/
  x86-64. iPXE has many features. Bergenholm uses some of them like
  HTTP downloading, iPXE scripting and per-host parameters.

* No Repository Inside; while Cobbler and MAAS have local repositories
  they manage, Bergenholm doesn't need them. Of course, you can build
  local repositories manually and make Bergenholm using them.

* REST APIs; Bergenholm has RESTful APIs for templates, hosts, groups
  and iPXE. No GUI/WebUI now.

* Parameter Inheritance; Bergenholm can handle JSON-style paraeters
  for host and group. host parameters can inherit group(s) parameters
  and group parameters can do too. No restriction for group definition.

* Jinja2 Templating; Bergenholm can handle Jinja2-style template files
  and parameters. You can use templates with host/group parameters for
  Kickstart/Preseed files, iPXE scripts, and so on.  Additionally, you
  can use parameters in parameters. No restriction for parameter
  usage except
  [reserved parameters](https://github.com/yosshy/bergenholm/blob/master/docs/RESERVED_PARAMS.md)
  .

* Streaming Remote Images; Bergenholm can fetch kernel/initrd images
  on remote sites and fowarding (streaming) them to installing
  targets.

* Power Management; Bergenholm can retrieve and change power status of
  installing targets. Supported power type are IPMI, VMware and
  Libvirt.

* Written in Flask-PyMongo and Flask-Action; So backend database is
  MongoDB. You can develop Bergenholm with Python.


## Structure

![Figure: Structure](https://github.com/yosshy/bergenholm/raw/master/docs/structure.png)


## Boot Sequence

(IT=Install Target, KS=Kickstart Install Server)

Common part:

1. IT: powered on (by pressing power button, IPMI, etc)
2. IT: sends DHCP request (by nic BIOS)
3. KS: sends DHCP response with next image information (by DHCP server)
4. IT: sends TFTP request for next image (by nic BIOS)
5. KS: sends iPXE image via TFTP (by TFTP server)
6. IT: sends HTTP request for iPXE script (by iPXE)
7. KS: sends iPXE script via HTTP (by Bergenholm)

Case-by-Case part:

(for installation)

8. IT: sends HTTP request to fetch boot images (by iPXE)
9. KS: fetches remote images via web proxy (by Bergenholm)
10. KS: sends images to IT via HTTP (by Bergenholm)

or (for local boot)

8. IT: boots from local storage (by iPXE)

or (for registration)

8.  IT: sends HTTP request to register IT itself to Bergenholm (by iPXE)
9.  KS: registers IT (by Bergenholm)
10. IT: boots from local storage (by iPXE)


## Install

See [INSTALL.md](https://github.com/yosshy/bergenholm/blob/master/docs/INSTALL.md)
for details.


## Usage

See [USAGE.md](https://github.com/yosshy/bergenholm/blob/master/docs/USAGE.md)
for details.
If you have bergenholmclient installed, you will like
[USAGE_CLI.md](https://github.com/yosshy/bergenholm/blob/master/docs/USAGE_CLI.md).


## Client

* [Command line tool](https://github.com/yosshy/bergenholmclient)


## APIs

See [API.md](https://github.com/yosshy/bergenholm/blob/master/docs/API.md)
for details.


## FAQs

See [FAQ.md](https://github.com/yosshy/bergenholm/blob/master/docs/FAQ.md).


## Notes

* ubuntu1404.preseed is based on
  https://github.com/wnoguchi/ubuntu_documents/tree/master/preseed
* centos6.kickstart is based on
  https://github.com/CentOS/Community-Kickstarts


## License

Apache License ver.2.0. See LICENSE for details.

Note: dhcp_server.py and centos6.kickstart are under GNU GPL
ver.2. ubuntu1404.preseed has no license displayed.
