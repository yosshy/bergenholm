# -*- encoding:utf-8 -*-
import logging
import jinja2

from flask import abort
from flask import json

from bergenholm.database.groups import get_group_params

mongo = None
jinja_env = jinja2.Environment()

INSTALLED = "installed"
UUID = "uuid"


def get_hosts():
    hosts = mongo.db.hosts.find({}, {'_id': 1})
    return {"hosts": [x["_id"] for x in hosts]}


def get_host(uuid):
    host = mongo.db.hosts.find_one_or_404({'_id': uuid})
    host.pop("_id", None)
    return host


def create_host(uuid, params):
    host = mongo.db.hosts.find_one({'_id': uuid})
    if host:
        abort(400)
    try:
        params['_id'] = uuid
        mongo.db.hosts.insert(params)
    except:
        abort(400)


def update_host(uuid, params):
    mongo.db.hosts.find_one_or_404({'_id': uuid})
    try:
        mongo.db.hosts.update({'_id': uuid}, params)
    except:
        abort(400)


def delete_host(uuid):
    mongo.db.hosts.find_one_or_404({'_id': uuid})
    try:
        mongo.db.hosts.remove({'_id': uuid})
    except:
        abort(400)


def render_string(temp_str, **params):
    if isinstance(temp_str, basestring):
        template = jinja_env.from_string(temp_str)
        return template.render(**params)
    elif isinstance(temp_str, (dict, list)):
        template = jinja_env.from_string(json.dumps(temp_str))
        return json.loads(template.render(**params))
    else:
        return temp_str


def get_host_params(uuid):
    host_params = mongo.db.hosts.find_one({'_id': uuid})
    if host_params is None:
        host_params = mongo.db.hosts.find_one({'_id': 'register'})
    if host_params is None:
        host_params = {}
    host_params.pop("_id", None)
    host_params[UUID] = uuid

    current_params, _groups = get_group_params(host_params.get('groups'))
    current_params.update(host_params)
    current_params["groups"] = _groups

    for i in range(10):
        new_params = {}
        for k, v in current_params.iteritems():
            k = render_string(k, **current_params)
            v = render_string(v, **current_params)
            new_params[k] = v
        if new_params == current_params:
            break
        current_params = new_params

    logging.debug(current_params)
    return current_params


def mark_host_installed(uuid):
    host = mongo.db.hosts.find_one_or_404({'_id': uuid})
    host.pop("_id", None)
    if INSTALLED in host["groups"]:
        abort(400)
    host["groups"].append(INSTALLED)
    try:
        mongo.db.hosts.update({'_id': uuid}, host)
    except:
        abort(400)


def unmark_host_installed(uuid):
    host = mongo.db.hosts.find_one_or_404({'_id': uuid})
    host.pop("_id", None)
    if INSTALLED not in host["groups"]:
        abort(400)
    host["groups"].remove(INSTALLED)
    try:
        mongo.db.hosts.update({'_id': uuid}, host)
    except:
        abort(400)
