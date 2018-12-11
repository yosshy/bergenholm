# Bergenholm REST API Reference


## Host APIs

Bergenholm has 6 host APIs. HTTP bodies of requests/responses are JSON.

### ```GET /api/1.0/hosts/```

Retrieve host list.

HTTP response:
- Status code:
  -  200 (success)
- Body:
  <pre>
  {
    "hosts": [
      "<uuid>",
      "<uuid>",
      ...,
    ]
  }
  </pre>


### ```GET /api/1.0/hosts/?<param>=<value>&<param>=<value>&...```

Retrieve filtered host list, hosts have parameters matching the condition specified as query parameters.
Matching is exact match. You can put multiple conditions and they will work as an AND condition.

HTTP response:
- Status code:
  -  200 (success)
- Body:
  <pre>
  {
    "hosts": [
      "<uuid>",
      "<uuid>",
      ...,
    ]
  }
  </pre>

### ```GET /api/1.0/hosts/<uuid>```

Retrieve host parameters.

HTTP request:
- uuid: host id

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body (example):
  <pre>
  {
    "groups": [
      "centos6",
      "centos.amd64"
    ],
    "hostname": "test-200",
    "ipaddr": "192.168.10.200"
  }
  </pre>

### ```GET /api/1.0/hosts/<uuid>?params=all```

Retrieve host parameters inherited its group parameters.

HTTP request:
- uuid: host id

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body (example):
  <pre>
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
    "kernel_opts": "ks=http://192.168.10.254/api/1.0/templates/centos6.kickstart/${uuid}",
    "kickstart": "centos6.kickstart",
    "mirror_url": "http://mirror.centos.org/centos-6/6/os/x86_64",
    "module": "http://mirror.centos.org/centos-6/6/os/x86_64/images/pxeboot/initrd.img",
    "nameserver": "192.168.0.254",
    "netmask": "255.255.255.0",
    "proxy_url": "http://proxy.example.com:8080",
    "uuid": "42cde8ca-835d-4271-9f82-82e902cc9505",
    "version": "6"
  }
  </pre>

### ```GET /api/1.0/hosts/<uuid>?installed=mark```

Append "installed" group to group list.

HTTP request:
- uuid: host id

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body: none

### ```GET /api/1.0/hosts/<uuid>?installed=unmark```

Remove "installed" group from grop list.

HTTP request:
- uuid: host id

HTTP response:
- Status code:
  - 204 (success)
  - 404 (uuid not found)
- Body: none

### ```POST /api/1.0/hosts/<uuid>```

Register host parameters.

HTTP request:
- uuid: host id
- Body (example):
  <pre>
  {
    "groups": [
      "centos6",
      "centos.amd64"
    ],
    "hostname": "test-200",
    "ipaddr": "192.168.10.200"
  }
  </pre>

HTTP response:
- Status code:
  - 201 (created)
  - 400 (uuid alredy exists / JSON is wrong)
- Body: none

### ```PUT /api/1.0/hosts/<uuid>```

Update host parameters.

HTTP request:
- uuid: host id
- Body (example):
<pre>
{
  "groups": [
    "centos6",
    "centos.amd64"
  ],
  "hostname": "test-200",
  "ipaddr": "192.168.10.200"
}
</pre>

HTTP response:
- Status code:
  - 202 (accepted)
  - 400 (JSON is wrong)
  - 404 (not found)
- Body: none

### ```DELETE /api/1.0/hosts/<uuid>```

Delete host parameters.

HTTP request:
- uuid: host id

HTTP response:
- Status code:
  - 204 (deleted)
  - 404 (not found)
- Body: none



## Group APIs

Bergenholm has 6 group APIs. HTTP bodies of requests/responses are JSON.

### ```GET /api/1.0/groups/```

Retrieve group list.

HTTP response:
- Status code:
  - 200 (success)
- Body (example):
  <pre>
  {
    "groups": [
      "centos",
      "centos6",
      "centos.amd64",
      "centos.x86",
      "default",
      "register",
      "ubuntu",
      "ubuntu1204",
      "ubuntu1404",
      "ubuntu1410",
      "ubuntu.amd64",
      "ubuntu.x86"
    ]
  }
  </pre>

### ```GET /api/1.0/groups/<name>```

Retrieve group parameters.

HTTP request:
- name: group name

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body (example):
  <pre>
  {
    "groups": [
      "default"
    ],
    "ipxe_script": "register.ipxe"
  }
  </pre>

### ```GET /api/1.0/groups/<name>?params=all```

Retrieve group parameters inherited its group parameters.

HTTP request:
- name: group name

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body (example):
  <pre>
  {
    "base_url": "http://192.168.10.254",
    "gateway": "192.168.10.254",
    "groups": [
      "default"
    ],
    "ipxe_script": "register.ipxe",
    "ipxe_url": "{{base_url}}/ipxe",
    "nameserver": "192.168.0.254",
    "netmask": "255.255.255.0",
    "proxy_url": "http://proxy.example.com:8080"
  }
  </pre>

### ```POST /api/1.0/groups/<name>```

Register group parameters.

HTTP request:
- name: group name
- Body (example):
  <pre>
  {
    "groups": [
      "default"
    ],
    "ipxe_script": "register.ipxe"
  }
  </pre>

HTTP response:
- Status code:
  - 201 (created)
  - 400 (uuid alredy exists / JSON is wrong)
- Body: none


### ```PUT /api/1.0/groups/<name>```

Update group parameters.

HTTP request:
- name: group name
- Body (example):
  <pre>
  {
    "groups": [
      "default"
    ],
    "ipxe_script": "register.ipxe"
  }
  </pre>

HTTP response:
- Status code:
  - 202 (accepted)
  - 400 (JSON is wrong)
  - 404 (not found)
- Body: none

### ```DELETE /api/1.0/groups/<name>```

Delete group parameters.

HTTP request:
- name: group name

HTTP response:
- Status code:
  - 204 (deleted)
  - 404 (not found)
- Body: none



## Template APIs

Bergenholm has 6 Template APIs. HTTP bodies of requests/responses are text.

### ```GET /api/1.0/templates/```

Retrieve template list.

HTTP response:

- Status code:
  - 200 (success)
- Body (example):
  <pre>
  {
    "templates": [
      "centos6.kickstart",
      "linux.ipxe",
      "ubuntu1404.preseed",
      "localboot.ipxe",
      "register.ipxe"
    ]
  }
  </pre>

### ```GET /api/1.0/templates/<name>```

Retrieve a template.

HTTP request:
- name: template name

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body (example):
  <pre>
  #!ipxe
  {% if kernel is defined %}
  {% if kernel_opts is defined %}
  kernel {{ipxe_url}}/kernel/${uuid} {{kernel_opts}}
  {% else %}
  kernel {{ipxe_url}}/kernel/${uuid}
  {% endif %}
  {% endif %}
  {% if module0 is defined %}
  module {{ipxe_url}}/module/${uuid}/0
  {% elif module is defined %}
  module {{ipxe_url}}/module/${uuid}
  {% endif %}
  {% if module1 is defined %}
  module {{ipxe_url}}/module/${uuid}/1
  {% endif %}
  {% if module2 is defined %}
  module {{ipxe_url}}/module/${uuid}/2
  {% endif %}
  {% if module3 is defined %}
  module {{ipxe_url}}/module/${uuid}/3
  {% endif %}
  boot
  </pre>

### ```GET /api/1.0/templates/<name>/<uuid>```

Render a template with host parameters specified.

HTTP request:
- name: template name
- uuid: host id

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body: template rendered with host parameters specified.

### ```POST /api/1.0/templates/<name>```

Register a template.

HTTP request:
- name: template name

- Body: any text file

HTTP response:
- Status code:
  - 201 (created)
  - 400 (uuid alredy exists / JSON is wrong)
- Body: none

### ```PUT /api/1.0/templates/<name>```

Update a template.

HTTP request:
- name: template name
- Body: any text file

HTTP response:
- Status code:
  - 202 (accepted)
  - 400 (JSON is wrong)
  - 404 (not found)
- Body: none

### ```DELETE /api/1.0/templates/<name>```

Delete a template.

HTTP request:
- name: template name

HTTP response:
- Status code:
  - 204 (deleted)
  - 404 (not found)
- Body: none



## iPXE APIs

### ```GET /ipxe/script/<uuid>```

Get an iPXE script rendered for host.

HTTP request:
- uuid: host id

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body (example):
  <pre>
  #!ipxe
  kernel http://192.168.10.254/ipxe/kernel/${uuid} ks=...
  module http://192.168.10.254/ipxe/module/${uuid}
  </pre>

### ```GET /ipxe/kernel/<uuid>```

Retrieve a kernel image for booting OS. It will be fetched from remote
site specified URL at "kernel" parameter.

HTTP request:
- uuid: host id

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body (example): vmlinuz image file

### ```GET /ipxe/initrd/kernel/<uuid>```
### ```GET /ipxe/module/kernel/<uuid>```
### ```GET /ipxe/initrd/kernel/<uuid>/<number>```
### ```GET /ipxe/module/kernel/<uuid>/<number>```

Retrieve a module (initrd) image for booting OS. It will be fetched
from remote site specified URL at "module" parameter or "module/0". If
number is specified, "```module<number>```" parameter is used.

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body (example): initrd image file

### ```GET /ipxe/register/<uuid>```

Register a host ```<uuid>``` to Bergenholm.

HTTP request:
- Parameter:
  - uuid: host id

HTTP response:
- Status code:
  - 201 (success)
  - 400 (uuid already exists)
- Body: none


## Power API

Bergenholm has 4 Power APIs. HTTP bodies ofresponses are JSON.

### `GET /api/1.0/power/status/<uuid>`

Retrieve power status of host `<uuid>`.

HTTP request:
- Parameter:
  - uuid: host id (UUID)

HTTP response:
- Status code:
  - 200 (success)
  - 404 (uuid not found)
- Body: 
  <pre>
  {
	"power": "on"
  }
  </pre>
  Note: power status is one of "on", "off" and "unknown".

### `PUT /api/1.0/power/<uuid>`

Change power state of host `<uuid>`.

HTTP request:
- Parameter:
  - uuid: host id
  <pre>
  {
	"power": "on"
  }
  </pre>
  Note: power status is one of "on", "off" and "reset".

HTTP response:
- Status code:
  - 202 (success)
  - 404 (uuid not found)
- Body: none
