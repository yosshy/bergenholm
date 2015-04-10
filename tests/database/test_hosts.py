import copy
from werkzeug import exceptions as exc

from tests import base
from bergenholm.database import hosts
from bergenholm.database.hosts import mongo


class HostsDatabaseTestCase(base.TestCase):

    def test_get_hosts(self):
        with self.app.test_request_context('/'):
            result = hosts.get_hosts()
            self.assertEqual(result, dict(hosts=[self.host_id]))

    def test_get_host(self):
        with self.app.test_request_context('/'):
            result = hosts.get_host(self.host_id)
            self.assertEqual(result, self.host_params)

    def test_create_host(self):
        with self.app.test_request_context('/'):
            result = hosts.create_host(self.host_id2,
                                       copy.copy(self.host_params2))
            self.assertEqual(result, None)
            result = hosts.get_host(self.host_id2)
            self.assertEqual(result, self.host_params2)

    def test_update_host(self):
        with self.app.test_request_context('/'):
            result = hosts.update_host(self.host_id,
                                       copy.copy(self.host_params2))
            self.assertEqual(result, None)
            result = hosts.get_host(self.host_id)
            self.assertEqual(result, self.host_params2)

    def test_delete_host(self):
        with self.app.test_request_context('/'):
            result = hosts.delete_host(self.host_id)
            self.assertEqual(result, None)
            self.assertRaises(exc.NotFound, hosts.get_host, self.host_id)

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
            u'test': u'test',
            u'uuid': self.host_id,
            u'power_driver': u'dummy'}
        with self.app.test_request_context('/'):
            result = hosts.get_host_params(self.host_id)
            self.assertEqual(result, expected)

    def test_mark_host_installed(self):
        with self.app.test_request_context('/'):
            result = hosts.mark_host_installed(self.host_id)
            params = copy.deepcopy(self.host_params)
            params["groups"].append("installed")
            result = hosts.get_host(self.host_id)
            self.assertEqual(result, params)

            result = hosts.unmark_host_installed(self.host_id)
            result = hosts.get_host(self.host_id)
            self.assertEqual(result, self.host_params)
