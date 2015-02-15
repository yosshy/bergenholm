from flask import json

from tests import base
from bergenholm.views import templates

API = "/api/1.0/templates/"


class TemplatesViewTestCase(base.TestCase):

    def test_get_templates(self):
        result = self.client.get(API)
        self.assertEqual(result.status_code, 200)

    def test_get_template(self):
        result = self.client.get(API + self.template_id)
        self.assertEqual(result.status_code, 200)

    def test_create_template(self):
        result = self.client.post(API + self.template_id2,
                                  data=json.dumps(self.template2),
                                  headers=self.headers)
        self.assertEqual(result.status_code, 201)
        result = self.client.get(API + self.template_id2)
        self.assertEqual(result.status_code, 200)

    def test_update_template(self):
        result = self.client.put(API + self.template_id,
                                 data=json.dumps(self.template2),
                                 headers=self.headers)
        self.assertEqual(result.status_code, 202)
        result = self.client.get(API + self.template_id)
        self.assertEqual(result.status_code, 200)

    def test_delete_template(self):
        result = self.client.delete(API + self.template_id)
        self.assertEqual(result.status_code, 204)
        result = self.client.get(API + self.template_id)
        self.assertEqual(result.status_code, 404)

    def test_get_template_render(self):
        expected = """test-200
        192.168.10.200
        http://127.0.0.1/images/linux
        http://127.0.0.1/images/initrd.gz
        http://127.0.0.1"""

        result = self.client.get(API + self.template_id + "/" + self.host_id)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, expected)
