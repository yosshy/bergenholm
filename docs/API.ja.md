# Bergenholm REST API リファレンス


## ホスト API

Bergenholm は６つのホスト API があります。HTTP リクエスト／レスポンスのボディは JSON 型です。

### ```GET /api/1.0/hosts/```

ホスト一覧を取得します。

HTTP レスポンス:
- ステータス
  -  200 (成功)
- ボディ
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

ホストのパラメータを取得します。

HTTP リクエスト:
- uuid: ホストのID (UUID)

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ(例):
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

グループのパラメータを継承したホストのパラメータを取得します。

HTTP リクエスト:
- uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ(例):
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

ホストのグループリストに installed グループを追加します。

HTTP リクエスト:
- uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (見つからない)
- ボディ: 無し

### ```GET /api/1.0/hosts/<uuid>?installed=unmark```

ホストのグループリストから installed グループを削除します。

HTTP リクエスト:
- uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 204 (成功)
  - 404 (見つからない)
- ボディ: 無し

### ```POST /api/1.0/hosts/<uuid>```

ホストのパラメータを登録します。

HTTP リクエスト:
- uuid: ホストID (UUID)
- ボディ(例):
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

HTTP レスポンス:
- ステータス:
  - 201 (作成成功)
  - 400 (同じ UUID がある／JSON が不正)
- ボディ: 無し

### ```PUT /api/1.0/hosts/<uuid>```

ホストのパラメータを更新します。

HTTP リクエスト:
- uuid: ホストID (UUID)
- ボディ(例):
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

HTTP レスポンス:
- ステータス:
  - 202 (成功)
  - 400 (JSON が不正)
  - 404 (見つからない)
- ボディ: 無し

### ```DELETE /api/1.0/hosts/<uuid>```

ホストのパラメータを削除します。

HTTP リクエスト:
- uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 204 (削除成功)
  - 404 (見つからない)
- ボディ: 無し


## グループ API

Bergenholm は６つのグループ API があります。HTTP リクエスト／レスポンスのボディは JSON 型です。

### ```GET /api/1.0/groups/```

グループ一覧を取得します。

HTTP レスポンス:
- ステータス:
  - 200 (成功)
- ボディ(例):
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

グループのパラメータを取得します。

HTTP リクエスト:
- name: グループ名

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ(例):
  <pre>
  {
    "groups": [
      "default"
    ],
    "ipxe_script": "register.ipxe"
  }
  </pre>

### ```GET /api/1.0/groups/<name>?params=all```

グループのパラメータを継承したホストのパラメータを取得します。

HTTP リクエスト:
- name: グループ名

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ(例):
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
    "proxy_url": "http://proxy.例.com:8080"
  }
  </pre>

### ```POST /api/1.0/groups/<name>```

グループのパラメータを登録します。

HTTP リクエスト:
- name: グループ名
- ボディ(例):
  <pre>
  {
    "groups": [
      "default"
    ],
    "ipxe_script": "register.ipxe"
  }
  </pre>

HTTP レスポンス:
- ステータス:
  - 201 (作成成功)
  - 400 (同じグループがある／JSON が不正)
- ボディ: 無し


### ```PUT /api/1.0/groups/<name>```

グループのパラメータを更新します。

HTTP リクエスト:
- name: グループ名
- ボディ(例):
  <pre>
  {
    "groups": [
      "default"
    ],
    "ipxe_script": "register.ipxe"
  }
  </pre>

HTTP レスポンス:
- ステータス:
  - 202 (成功)
  - 400 (JSON が不正)
  - 404 (見つからない)
- ボディ: 無し

### ```DELETE /api/1.0/groups/<name>```

グループのパラメータを削除します。

HTTP リクエスト:
- name: グループ名

HTTP レスポンス:
- ステータス:
  - 204 (削除成功)
  - 404 (見つからない)
- ボディ: 無し



## テンプレート API

Bergenholm は６つのテンプレート API があります。HTTP リクエスト／レスポンスのボディはテキストです。

### ```GET /api/1.0/templates/```

テンプレート一覧を取得します。

HTTP レスポンス:
- ステータス:
  - 200(成功)
- ボディ (例):
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

テンプレートを取得します。

HTTP リクエスト:
- name: テンプレート名

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ(例):
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

ホストのパラメータでレンダリングしたテンプレートを取得します。

HTTP リクエスト:
- name: テンプレート名
- uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ: 指定されたホストのパラメータによるテンプレートのレンダリング結果


### ```POST /api/1.0/templates/<name>```

テンプレートを登録します。

HTTP リクエスト:
- name: テンプレート名
- ボディ: 任意のテキストファイル

HTTP レスポンス:
- ステータス:
  - 201 (作成成功)
  - 400 (同じ UUID がある／JSON が不正)
- ボディ: 無し

### ```PUT /api/1.0/templates/<name>```

テンプレートを更新します。

HTTP リクエスト:
- name: テンプレート名
- ボディ: 任意のテキスト

HTTP レスポンス:
- ステータス:
  - 202 (成功)
  - 400 (JSON が不正)
  - 404 (見つからない)
- ボディ: 無し

### ```DELETE /api/1.0/templates/<name>```

テンプレートを削除します。

HTTP リクエスト:
- name: テンプレート名

HTTP レスポンス:
- ステータス:
  - 204 (削除成功)
  - 404 (見つからない)
- ボディ: 無し



## iPXE API

### ```GET /ipxe/script/<uuid>```

ホスト用にレンダリングされた iPXE スクリプトを取得します。

HTTP リクエスト:
- uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ(例):
  <pre>
  #!ipxe
  kernel http://192.168.10.254/ipxe/kernel/${uuid} ks=...
  module http://192.168.10.254/ipxe/module/${uuid}
  </pre>

### ```GET /ipxe/kernel/<uuid>```

起動 OS のカーネルイメージを取得します。ホスト／グループの kernel パラ
メータの URL で指定されたリモートサイトからイメージを取得します。

HTTP リクエスト:
- uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ(例): vmlinuz イメージファイル

### ```GET /ipxe/initrd/kernel/<uuid>```
### ```GET /ipxe/module/kernel/<uuid>```
### ```GET /ipxe/initrd/kernel/<uuid>/<number>```
### ```GET /ipxe/module/kernel/<uuid>/<number>```

起動 OS のモジュール(initrd)イメージを取得します。ホスト／グループの
module パラメータ又は module/0 の URL で指定されたリモートサイトからイ
メージを取得します。number が指定された場合、イメージ取得元として
```module<number>``` パラメータの URL が使用されます。

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ(例): initrd イメージファイル

### ```GET /ipxe/register/<uuid>```

Bergenholm にホスト uuid を登録します。

HTTP リクエスト:
- パラメータ:
  - uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 201 (成功)
  - 400 (同じ UUID がある)
- ボディ: 無し



## 電源API

Bergenholm は４つの電源 API があります。HTTP レスポンスのボディは JSON 形です。

### `GET /api/1.0/power/<uuid>`

ホスト`<uuid>`の電源状況（On/Off）を取得します。

HTTP リクエスト:
- パラメータ:
  - uuid: ホストID (UUID)

HTTP レスポンス:
- ステータス:
  - 200 (成功)
  - 404 (UUID が見つからない)
- ボディ: 
  <pre>
  {
	"power": "on"
  }
  </pre>
  ※電源状態は "on", "off", "unknown" の３種類

### `PUT /api/1.0/power/<uuid>`

ホスト`<uuid>`の電源状態を変更します。

HTTP リクエスト:
- パラメータ:
  - uuid: ホストID (UUID)
- ボディ:
  <pre>
  {
	"power": "on"
  }
  </pre>
  ※電源状態は "on", "off", "reset の３種類

HTTP レスポンス:
- ステータス:
  - 202 (成功)
  - 404 (UUID が見つからない)
- ボディ: 無し
