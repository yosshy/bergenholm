# -*- encoding:utf-8 -*-
import logging

from flask import (
    Blueprint, Response,
    current_app,
    abort, jsonify, redirect, stream_with_context, request,
    render_template, render_template_string, make_response
)

from bergenholm.database.hosts import (
    get_host, get_hosts, create_host, update_host, delete_host,
    get_host_params, mark_host_installed, unmark_host_installed
)


hosts = Blueprint('hosts', __name__)


@hosts.route('')
@hosts.route('/')
def _list():
    return jsonify(get_hosts(request.args))


@hosts.route('/<name>',  methods=["POST"])
def _create(name):
    params = request.get_json()
    if not isinstance(params, dict):
        abort(400)
    create_host(name, request.get_json())
    return make_response("", 201, [])


@hosts.route('/<uuid>')
def _get(uuid):
    if request.args.get('installed') == 'mark':
        mark_host_installed(uuid)
        return make_response("", 200, [])
    if request.args.get('installed') == 'unmark':
        unmark_host_installed(uuid)
        return make_response("", 200, [])
    if request.args.get('params') == 'all':
        return jsonify(get_host_params(uuid))
    return jsonify(get_host(uuid))


@hosts.route('/<uuid>',  methods=["PUT"])
def _update(uuid):
    params = request.get_json()
    if not isinstance(params, dict):
        abort(400)
    update_host(uuid, params)
    return make_response("", 202, [])


@hosts.route('/<uuid>',  methods=["DELETE"])
def _delete(uuid):
    delete_host(uuid)
    return make_response("", 204, [])
