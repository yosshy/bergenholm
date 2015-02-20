from flask import json
from mock import patch, call, ANY
import requests

from tests import base
from bergenholm.views import groups

API = "/ipxe"


class IpxeViewTestCase(base.TestCase):

    def test_script(self):
        expected = """test-200
        192.168.10.200
        http://127.0.0.1/images/linux
        http://127.0.0.1/images/initrd.gz
        http://127.0.0.1"""
        result = self.client.get(API + "/script/" + self.host_id)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, expected)

    @patch('requests.get')
    def test_kernel(self, patched):
        result = self.client.get(API + "/kernel/" + self.host_id)
        self.assertEqual(result.status_code, 200)
        patched.assert_any_call(
            u'http://127.0.0.1/images/linux', proxies=None, stream=True)

    @patch('requests.get')
    def test_module(self, patched):
        result = self.client.get(API + "/module/" + self.host_id)
        self.assertEqual(result.status_code, 200)
        patched.assert_any_call(
            u'http://127.0.0.1/images/initrd.gz', proxies=None, stream=True)
        result = self.client.get(API + "/module/%s/0" % self.host_id)
        self.assertEqual(result.status_code, 301)
        self.assertEqual(result.headers["Location"],
                         'http://localhost/ipxe/module/'
                         '352acfdb-ef72-4d2d-b76d-7be95cde6deb')
        result = self.client.get(API + "/module/%s/1" % self.host_id)
        self.assertEqual(result.status_code, 200)
        result = self.client.get(API + "/module/%s/2" % self.host_id)
        self.assertEqual(result.status_code, 404)

    @patch('requests.get')
    def test_initrd(self, patched):
        result = self.client.get(API + "/initrd/" + self.host_id)
        self.assertEqual(result.status_code, 301)
        self.assertEqual(result.headers["Location"],
                         'http://localhost/ipxe/module/'
                         '352acfdb-ef72-4d2d-b76d-7be95cde6deb')
        result = self.client.get(API + "/initrd/%s/0" % self.host_id)
        self.assertEqual(result.status_code, 301)
        self.assertEqual(result.headers["Location"],
                         'http://localhost/ipxe/module/'
                         '352acfdb-ef72-4d2d-b76d-7be95cde6deb')
        result = self.client.get(API + "/initrd/%s/1" % self.host_id)
        self.assertEqual(result.status_code, 200)
        result = self.client.get(API + "/initrd/%s/2" % self.host_id)
        self.assertEqual(result.status_code, 404)

    def test_register(self):
        result = self.client.get("/api/1.0/hosts/" + self.host_id2)
        self.assertEqual(result.status_code, 404)
        result = self.client.get(API + "/register/" + self.host_id2)
        self.assertEqual(result.status_code, 201)
        result = self.client.get("/api/1.0/hosts/" + self.host_id2)
        self.assertEqual(result.status_code, 200)
