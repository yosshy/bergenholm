from flask import json

from tests import base
from bergenholm.views import groups

API = "/api/1.0/groups/"


class GroupsViewTestCase(base.TestCase):

    headers = {"Content-Type": "application/json"}

    def test_get_groups(self):
        expected = {u"groups": [u"default", self.group_id]}
        result = self.client.get(API)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), expected)

    def test_get_group(self):
        result = self.client.get(API + self.group_id)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), self.group_params)

    def test_create_group(self):
        result = self.client.post(API + self.group_id2,
                                  data=json.dumps(self.group_params2),
                                  headers=self.headers)
        self.assertEqual(result.status_code, 201)
        result = self.client.get(API + self.group_id2)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), self.group_params2)

    def test_update_group(self):
        result = self.client.put(API + self.group_id,
                                 data=json.dumps(self.group_params2),
                                 headers=self.headers)
        self.assertEqual(result.status_code, 202)
        result = self.client.get(API + self.group_id)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), self.group_params2)

    def test_delete_group(self):
        result = self.client.delete(API + self.group_id)
        self.assertEqual(result.status_code, 204)
        result = self.client.get(API + self.group_id)
        self.assertEqual(result.status_code, 404)

    def test_get_group_params(self):
        expected = {
            u'kernel': u'{{image_base_url}}/linux',
            u'image_base_url': u'{{base_url}}/images',
            u'mirror_path': u'/ubuntu',
            u'mirror_scheme': u'http',
            u'base_url': u'http://127.0.0.1',
            u'module': u'{{image_base_url}}/initrd.gz',
            u'module1': u'{{image_base_url}}/initrd1.gz',
            u'kernel_opts': u'quiet',
            u'ipxe_script': u'ubuntu.temp',
            u'groups': [u'default'],
            u'mirror_host': u'jp.archive.ubuntu.com'
        }

        result = self.client.get(API + self.group_id + "?params=all")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), expected)
