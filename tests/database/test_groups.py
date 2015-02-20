import copy
from werkzeug import exceptions as exc

from tests import base
from bergenholm.database import groups
from bergenholm.database.groups import mongo


class GroupsDatabaseTestCase(base.TestCase):

    def test_get_groups(self):
        with self.app.test_request_context('/'):
            result = groups.get_groups()
            self.assertEqual(result, dict(groups=[u"default", self.group_id]))

    def test_get_group(self):
        with self.app.test_request_context('/'):
            result = groups.get_group(self.group_id)
            self.assertEqual(result, self.group_params)

    def test_create_group(self):
        with self.app.test_request_context('/'):
            result = groups.create_group(self.group_id2,
                                         copy.copy(self.group_params2))
            self.assertEqual(result, None)
            result = groups.get_group(self.group_id2)
            self.assertEqual(result, self.group_params2)

    def test_update_group(self):
        with self.app.test_request_context('/'):
            result = groups.update_group(self.group_id,
                                         copy.copy(self.group_params2))
            self.assertEqual(result, None)
            result = groups.get_group(self.group_id)
            self.assertEqual(result, self.group_params2)

    def test_delete_group(self):
        with self.app.test_request_context('/'):
            result = groups.delete_group(self.group_id)
            self.assertEqual(result, None)
            self.assertRaises(exc.NotFound, groups.get_group, self.group_id)

    def test_get_group_params(self):
        expected_params = {
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
        expected_groups = [u'ubuntu', u'default']
        with self.app.test_request_context('/'):
            _params, _groups = groups.get_group_params(self.group_id)
            self.assertEqual(_params, expected_params)
            self.assertEqual(_groups, expected_groups)
