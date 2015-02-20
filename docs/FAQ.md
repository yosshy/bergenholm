# Bergenholm: FAQs


## What is Bergenholm?

Bergenholm is a kickstart install server like below:
* Cobbler (http://www.cobblerd.org/)
* MAAS (https://maas.ubuntu.com/)

## How distinctive is Bergenholm?

Bergenholm is a simple and small program, but it has significant features.

* Only REST APIs
* Using iPXE (http://ipxe.org/) efficiently
* No repository inside
* Parameter inheritance from groups
* Jinja2 templating for iPXE script, kickstart/preseed and other usages
* Streaming Remote Images (via web proxy)
* Written in Flask-PyMongo

## Why Bergenholm was created?

* Local repositories are useful for mass servers installation, but not
  necessary for only one or a few. MAAS and Cobbler aren't fit at the
  case because they need to have local repositories. Bergenholm
  doesn't, but it can be used with the existing repos.

* MAAS and Cobbler are too complex to be developed. Bergenholm is
  Flask based, so it's easy to learn and hack it.

* iPXE is a new and cool network bootloader, especially image fetching
  via HTTP. But there is no software that use it efficiently.
  Bergenholm may be the first one.

* Cobbler handles distros, profiles, sub-profiles, systems, images and
  repos and these parameters can be inherited. But they are complex,
  not flexible and not allowed for multiple inheritance. Bergenholm
  has only 2 parameter classese "host" and "group". "host" and "group"
  can inherit parameters of groups specified "groups" parameter in
  them. As you expected, "groups" paraeter is a list of group names.

* It's hard to build HA cluster for Cobbler and MAAS because of their
  managing DHCP (and DNS). Bergenholm is a kind of just web
  application and it doesn't manage DHCP settings, so it's easy to
  build its HA/LB clusters.

## Why named "Bergenholm"?

"Bergenholm space drive" is the name of faster-than-light (FTL)
transportation technology of Lensman series.
http://en.wikipedia.org/wiki/Bergenholm_space_drive

* Looking for name of FTL technology like Ansible.
* No existing software (especially OSS) named it.
* bergenholm.com is free now.

## What about authentication?

Apache HTTPD and Nginx are useful for it.

## How to use a local repository?

Modify linux.ipxe or register a new .ipxe template like below:

<pre>
#!ipxe
kernel {{repos_url}}/path/to/vmlinuz ks=...
module {{repos_url}}/path/to/initrd
boot
</pre>

You have to specify the new .ipxe template in host/group parameters if
you added it.
