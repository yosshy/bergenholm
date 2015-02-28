from flask import json
from mock import patch, call, ANY
import requests

from tests import base

API = "/api/1.0/power/"


class PowerViewTestCase(base.TestCase):

    @patch('requests.get')
    def test_power_status(self, patched):
        expected = '{\n  "power": "on"\n}'
        result = self.client.get(API + self.host_id)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, expected)

    @patch('requests.put')
    def test_power_on(self, patched):
        result = self.client.put(API + self.host_id,
                                 data='{"power": "on"}',
                                 headers=self.headers)
        self.assertEqual(result.status_code, 202)

    @patch('requests.put')
    def test_power_off(self, patched):
        result = self.client.put(API + self.host_id,
                                 data='{"power": "off"}',
                                 headers=self.headers)
        self.assertEqual(result.status_code, 202)

    @patch('requests.put')
    def test_power_reset(self, patched):
        result = self.client.put(API + self.host_id,
                                 data='{"power": "reset"}',
                                 headers=self.headers)
        self.assertEqual(result.status_code, 202)
