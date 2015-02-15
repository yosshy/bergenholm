# -*- encoding:utf-8 -*-
import logging

from flask import (
    Blueprint, Response,
    current_app,
    abort, jsonify, make_response, request,
    render_template, render_template_string,
    stream_with_context
)

from bergenholm.database.templates import (
    get_template, get_templates, create_template, update_template,
    delete_template
)

from bergenholm.database.hosts import get_host_params

templates = Blueprint('templates', __name__)


@templates.route('')
@templates.route('/')
def _list():
    return make_response(jsonify(get_templates()))


@templates.route('/<name>',  methods=["POST"])
def _create(name):
    create_template(name, request.get_data())
    return make_response("", 201, [])


@templates.route('/<name>')
def _get(name):
    return make_response(get_template(name))


@templates.route('/<name>/<uuid>')
def _render(name, uuid):
    try:
        template = get_template(name)
        params = get_host_params(uuid)
        return render_template_string(template, **params)
    except KeyError:
        return abort(404)


@templates.route('/<name>',  methods=["PUT"])
def _update(name):
    update_template(name, request.get_data())
    return make_response("", 202, [])


@templates.route('/<name>',  methods=["DELETE"])
def _delete(name):
    delete_template(name)
    return make_response("", 204, [])
