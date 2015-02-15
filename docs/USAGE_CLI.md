Bergenholm: Basic Usage with bergenholmclient
=============================================


After installing bergenholm and bergenholmclient, 

1. Power on of a install-target by hand.
   If it started network booting started, you will see a message on the screen:
   <pre>
   ...
   ===== System UUID is XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX =====
   ===== Registering this host to Bergenholm =====
   ...
   ===== Trying boot from local disk =====
   </pre>
   XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX is the system UUID of your install-target.
2. Ckeck the entry for it on the kickstart install server.
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
3. Get a sample parameter file.
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
   There are 3 paraemters; "groups", "hostname" and "ipaddr". You can modify values.
   If you want to install Ubuntu 14.04, you have to modify "groups" parameter like below:
   <pre>
     "groups": [
       "ubuntu1404",
       "ubuntu.amd64"
     ],
   </pre>
4. Modify parameters of the install-target.
   <pre>
   $ bergenholmclient host update XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX /tmp/params
   </pre>
5. Reboot the install-target, then it will start kickstart install sequence.
6. Restore default parameters to boot the install-target from local storage.
   <pre>
   $ bergenholmclient host update XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX /tmp/default
   </pre>
