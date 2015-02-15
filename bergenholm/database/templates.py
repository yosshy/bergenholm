# -*- encoding:utf-8 -*-
import logging
import jinja2

from flask import abort
from flask import json

mongo = None
jinja_env = jinja2.Environment()


def get_templates():
    templates = mongo.db.templates.find({}, {'_id': 1})
    return dict(templates=[t["_id"] for t in templates])


def get_template(name):
    template = mongo.db.templates.find_one_or_404({'_id': name})
    template.pop("_id", None)
    return template["content"]


def create_template(name, content):
    template = mongo.db.templates.find_one({'_id': name})
    if template:
        abort(400)
    try:
        mongo.db.templates.insert(dict(_id=name, content=content))
    except:
        abort(400)


def update_template(name, content):
    mongo.db.templates.find_one_or_404({'_id': name})
    try:
        mongo.db.templates.update({'_id': name},
                                  {"$set": dict(content=content)})
    except:
        abort(400)


def delete_template(name):
    mongo.db.templates.find_one_or_404({'_id': name})
    try:
        mongo.db.templates.remove({'_id': name})
    except:
        abort(400)
