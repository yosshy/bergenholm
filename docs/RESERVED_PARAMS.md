# Bergenholm: Reserved Parameters

## proxy_url

URL of HTTP Proxy. If set, Bergenholm uses a HTTP proxy specified by
proxy_url for downloading kernel/module images.

## ipxe_script

Template name for iPXE script. Bergenholm returns rendered result with
a template specified with ipxe_script and host parameters specified
with uuid when "```GET /ipxe/script/<uuid>```" is required.

## kernel

URL of remote kernel image. Bergenholm uses it to download a kernel
image when "```GET /ipxe/kernel/<uuid>```" is required.

## module

URL of remote module (initrd) image. Bergenholm uses it to download a
module image for:

* ```GET /ipxe/module/<uuid>```
* ```GET /ipxe/module/<uuid>/0```
* ```GET /ipxe/initrd/<uuid>```
* ```GET /ipxe/initrd/<uuid>/0```

## moduleN (N=0-; integer)

URL of remote module (initrd) image. Bergenholm uses it to download a
module image for:

* ```GET /ipxe/module/<uuid>/<N>```
* ```GET /ipxe/initrd/<uuid>/<N>```
