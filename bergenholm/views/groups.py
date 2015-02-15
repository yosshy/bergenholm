# -*- encoding:utf-8 -*-
import logging

from flask import (
    Blueprint, Response,
    current_app,
    abort, jsonify, redirect, stream_with_context, request,
    render_template, render_template_string, make_response
)

from bergenholm.database.groups import (
    get_group, get_groups, create_group, update_group, delete_group,
    get_group_params
)


groups = Blueprint('groups', __name__)


@groups.route('')
@groups.route('/')
def _list():
    return jsonify(get_groups())


@groups.route('/<name>',  methods=["POST"])
def _create(name):
    params = request.get_json()
    if not isinstance(params, dict):
        abort(400)
    create_group(name, request.get_json())
    return make_response("", 201, [])


@groups.route('/<name>')
def _get(name):
    if request.args.get('params') == 'all':
        params, _groups = get_group_params(name)
        return jsonify(params)
    return jsonify(get_group(name))


@groups.route('/<name>',  methods=["PUT"])
def _update(name):
    params = request.get_json()
    if not isinstance(params, dict):
        abort(400)
    update_group(name, params)
    return make_response("", 202, [])


@groups.route('/<name>',  methods=["DELETE"])
def _delete(name):
    delete_group(name)
    return make_response("", 204, [])
