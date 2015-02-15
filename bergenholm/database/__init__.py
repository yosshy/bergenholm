# -*- encoding:utf-8 -*-
from flask.ext.pymongo import PyMongo

from bergenholm.database import hosts
from bergenholm.database import groups
from bergenholm.database import templates

mongo = None


def init_db(app):
    global mongo
    mongo = PyMongo(app)
    hosts.mongo = mongo
    groups.mongo = mongo
    templates.mongo = mongo
