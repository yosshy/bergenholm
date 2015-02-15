import unittest

from flask import Flask
from flaskext.actions import Manager

import settings

from bergenholm import database


from bergenholm.views.frontend import frontend
from bergenholm.views.ipxe import ipxe
from bergenholm.views.hosts import hosts
from bergenholm.views.groups import groups
from bergenholm.views.templates import templates


class TestCase(unittest.TestCase):

    headers = {"Content-Type": "application/json"}

    host_id = u"352acfdb-ef72-4d2d-b76d-7be95cde6deb"
    host_params = {
        u"hostname": u"test-200",
        u"ipaddr": u"192.168.10.200",
        u"groups": [u"ubuntu"],
        u"test": u"test"
    }

    host_id2 = u"6ab07bc6-2ee4-4ae9-b9b7-4c27806b640e"
    host_params2 = {
        u"groups": [
            u"centos6",
            u"centos.amd64"
        ],
        u"hostname": u"test-200",
        u"ipaddr": u"192.168.10.200"
    }

    group_id = u"ubuntu"
    group_params = {
        u"groups": [u"default"],
        u"mirror_scheme": u"http",
        u"mirror_host": u"jp.archive.ubuntu.com",
        u"mirror_path": u"/ubuntu",
        u"image_base_url": u"{{base_url}}/images",
        u"kernel": u"{{image_base_url}}/linux",
        u"module": u"{{image_base_url}}/initrd.gz",
        u"kernel_opts": u"quiet",
        u"ipxe_script": u"linux.ipxe"
    }

    group_id2 = u"centos"
    group_params2 = {
        u"groups": [u"default"],
        u"mirror_url": u"{{base_url}}/centos",
        u"image_base_url": u"{{mirror_url}}/images/pxeboot",
        u"kernel": u"{{image_base_url}}/vmlinuz",
        u"module": u"{{image_base_url}}/initrd.img",
        u"api_url": u"{{base_url}}/api/1.0",
        u"kernel_opts": u"ks={{api_url}}/templates/{{kickstart}}/${uuid}",
        u"ipxe_script": u"linux.ipxe"
    }

    template_id = u"ubuntu.temp"
    template = u"""{{hostname}}
        {{ipaddr}}
        {{kernel}}
        {{module}}
        {{base_url}}"""

    template_id2 = u"centos.temp"
    template2 = u"""
        {{kernel}}
        {{module}}
        {{hostname}}
    """

    def setUp(self):
        app = Flask(__name__)
        app.config.from_object(settings)
        app.testing = True
        app.config['MONGO_DBNAME'] = 'bergenholmtest'
        database.init_db(app)

        app.register_blueprint(frontend, url_prefix='')
        app.register_blueprint(ipxe, url_prefix='/ipxe')
        app.register_blueprint(hosts, url_prefix='/api/1.0/hosts')
        app.register_blueprint(groups, url_prefix='/api/1.0/groups')
        app.register_blueprint(templates, url_prefix='/api/1.0/templates')

        self.app = app
        self.client = app.test_client()
        self.mongo = database.mongo

        with self.app.test_request_context('/'):
            self.mongo.db.hosts.remove()
            self.mongo.db.groups.remove()
            self.mongo.db.templates.remove()

            params = {u"_id": self.host_id}
            params.update(self.host_params)
            self.mongo.db.hosts.insert(params)

            self.mongo.db.groups.insert({
                u"_id": u"default",
                u"base_url": u"http://127.0.0.1"})

            params = {u"_id": self.group_id}
            params.update(self.group_params)
            self.mongo.db.groups.insert(params)

            self.mongo.db.templates.insert({
                u"_id": self.template_id,
                u"content": self.template})

    def tearDown(self):
        with self.app.test_request_context('/'):
            self.mongo.db.hosts.remove()
            self.mongo.db.groups.remove()
            self.mongo.db.templates.remove()
