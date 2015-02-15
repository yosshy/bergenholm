# -*- encoding:utf-8 -*-
import logging
import jinja2

from flask import abort
from flask import json

mongo = None
jinja_env = jinja2.Environment()


def get_groups():
    groups = mongo.db.groups.find({}, {'_id': 1})
    return {"groups": [x["_id"] for x in groups]}


def get_group(name):
    group = mongo.db.groups.find_one_or_404({'_id': name})
    group.pop("_id")
    return group


def create_group(name, params):
    group = mongo.db.groups.find_one({'_id': name})
    if group:
        abort(400)
    try:
        params['_id'] = name
        mongo.db.groups.insert(params)
    except:
        abort(400)


def update_group(name, params):
    mongo.db.groups.find_one_or_404({'_id': name})
    try:
        mongo.db.groups.update({'_id': name}, params)
    except:
        abort(400)


def delete_group(name):
    mongo.db.groups.find_one_or_404({'_id': name})
    try:
        mongo.db.groups.remove({'_id': name})
    except:
        abort(400)


def get_group_params(groups, current_groups=None):
    if current_groups is None:
        current_groups = []
    if groups is None:
        return {}, current_groups

    new_params = {}
    if isinstance(groups, basestring):
        groups = [groups]
    elif not isinstance(groups, list):
        abort(400)

    for group in groups:
        if not isinstance(group, basestring):
            abort(400)
        if group in current_groups:
            continue
        current_groups.append(group)

        current_params = mongo.db.groups.find_one({'_id': group})
        current_params.pop("_id", None)
        next_groups = current_params.get('groups')
        next_params, current_groups = get_group_params(next_groups,
                                                       current_groups)
        new_params.update(next_params)
        new_params.update(current_params)

    return new_params, current_groups
