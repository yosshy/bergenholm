import copy
from werkzeug import exceptions as exc

from tests import base
from bergenholm.database import templates
from bergenholm.database.templates import mongo


class TemplatesDatabaseTestCase(base.TestCase):

    def test_get_templates(self):
        with self.app.test_request_context('/'):
            result = templates.get_templates()
            self.assertEqual(result, dict(templates=[self.template_id]))

    def test_get_template(self):
        with self.app.test_request_context('/'):
            result = templates.get_template(self.template_id)
            self.assertEqual(result, self.template)

    def test_create_template(self):
        with self.app.test_request_context('/'):
            result = templates.create_template(self.template_id2,
                                               copy.copy(self.template2))
            self.assertEqual(result, None)
            result = templates.get_template(self.template_id2)
            self.assertEqual(result, self.template2)

    def test_update_template(self):
        with self.app.test_request_context('/'):
            result = templates.update_template(self.template_id,
                                               copy.copy(self.template2))
            self.assertEqual(result, None)
            result = templates.get_template(self.template_id)
            self.assertEqual(result, self.template2)

    def test_delete_template(self):
        with self.app.test_request_context('/'):
            result = templates.delete_template(self.template_id)
            self.assertEqual(result, None)
            self.assertRaises(exc.NotFound,
                              templates.get_template, self.template_id)
