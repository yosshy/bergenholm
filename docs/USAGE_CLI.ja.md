# Bergenholm: bergenholmclient による使用法


bergenholm と bergenholmclient インストール後、

1. インストール先サーバを手動で起動します。ネットワークブートが開始され
   ると、スクリーンに以下のメッセージが表示されます。

   <pre>
   ...
   ===== System UUID is XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX =====
   ===== Registering this host to Bergenholm =====
   ...
   ===== Trying boot from local disk =====
   </pre>

   XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX はインストール先サーバのシステ
   ム UUID です。

2. キックスタートインストールサーバ上のホストエントリを確認します。

   <pre>
   $ bergenholmclient host list
   samplehost
   default
   register
   XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
   $ bergenholmclient host show XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX > /tmp/default
   $ cat /tmp/default
   {
     "groups": [
       "default"
     ]
   }
   </pre>

3. サンプルのパラメータファイルを取得します。

   <pre>
   $ bergenholmclient host show samplehost > /tmp/params
   $ cat /tmp/params
   {
     "groups": [
       "centos6",
       "centos.amd64"
     ],
     "hostname": "test-200",
     "ipaddr": "192.168.10.200"
   }
   </pre>

   groups、hostname、ipaddr の３パラメータがあり、変更可能です。Ubuntu
   14.04 をインストールする場合、groups パラメータを下記のように変更し
   ます。

   <pre>
     "groups": [
       "ubuntu1404",
       "ubuntu.amd64"
     ],
   </pre>

4. 取得したパラメータファイルインストール先サーバ用に修正します。

   <pre>
   $ bergenholmclient host update XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX /tmp/params
   </pre>

5. インストール先サーバを再起動すると、キックスタートインストールが開始
   されます。

6. インストール後、インストール先サーバのパラメータをデフォルトのローカ
   ルストレージ起動に戻します。

   <pre>
   $ bergenholmclient host update XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX /tmp/default
   </pre>
