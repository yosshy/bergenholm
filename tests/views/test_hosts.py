from flask import json

from tests import base
from bergenholm.views import hosts

API = "/api/1.0/hosts/"


class HostsViewTestCase(base.TestCase):

    def test_get_hosts(self):
        expected = {u"hosts": [self.host_id]}
        result = self.client.get(API)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), expected)

    def test_get_host(self):
        result = self.client.get(API + self.host_id)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), self.host_params)

    def test_create_host(self):
        result = self.client.post(API + self.host_id2,
                                  data=json.dumps(self.host_params2),
                                  headers=self.headers)
        self.assertEqual(result.status_code, 201)
        result = self.client.get(API + self.host_id2)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), self.host_params2)

    def test_update_host(self):
        result = self.client.put(API + self.host_id,
                                 data=json.dumps(self.host_params2),
                                 headers=self.headers)
        self.assertEqual(result.status_code, 202)
        result = self.client.get(API + self.host_id)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), self.host_params2)

    def test_delete_host(self):
        result = self.client.delete(API + self.host_id)
        self.assertEqual(result.status_code, 204)
        result = self.client.get(API + self.host_id)
        self.assertEqual(result.status_code, 404)

    def test_get_host_params(self):
        expected = {
            u'base_url': u'http://127.0.0.1',
            u'groups': [u'ubuntu', u'default'],
            u'hostname': u'test-200',
            u'image_base_url': u'http://127.0.0.1/images',
            u'ipaddr': u'192.168.10.200',
            u'ipxe_script': u'ubuntu.temp',
            u'kernel': u'http://127.0.0.1/images/linux',
            u'kernel_opts': u'quiet',
            u'mirror_host': u'jp.archive.ubuntu.com',
            u'mirror_path': u'/ubuntu',
            u'mirror_scheme': u'http',
            u'module': u'http://127.0.0.1/images/initrd.gz',
            u'module1': u'http://127.0.0.1/images/initrd1.gz',
            u'power_driver': 'dummy',
            u'test': u'test'}

        result = self.client.get(API + self.host_id + "?params=all")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), expected)
