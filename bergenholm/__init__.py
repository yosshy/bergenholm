# -*- encoding:utf-8 -*-
from flask import Flask

from bergenholm import database

from bergenholm.views.frontend import frontend
from bergenholm.views.ipxe import ipxe
from bergenholm.views.hosts import hosts
from bergenholm.views.groups import groups
from bergenholm.views.templates import templates

app = Flask(__name__)
database.init_db(app)

app.register_blueprint(frontend, url_prefix='')
app.register_blueprint(ipxe, url_prefix='/ipxe')
app.register_blueprint(hosts, url_prefix='/api/1.0/hosts')
app.register_blueprint(groups, url_prefix='/api/1.0/groups')
app.register_blueprint(templates, url_prefix='/api/1.0/templates')
