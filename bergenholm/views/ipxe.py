# -*- encoding:utf-8 -*-
import requests

from flask import (
    Blueprint, Response,
    abort, stream_with_context, make_response,
    render_template_string
)

from bergenholm.database.hosts import get_host_params, create_host
from bergenholm.database.templates import get_template


# chunk_size = 1MB
CHUNK_SIZE = 1024 * 1024

ipxe = Blueprint('ipxe', __name__)


@ipxe.route('/script/<uuid>')
def script(uuid):
    try:
        params = get_host_params(uuid)
        template = get_template(params["ipxe_script"])
        return render_template_string(template, **params)
    except KeyError:
        return abort(404)


def proxy(url, params):
    proxies = None
    if "proxy_url" in params:
        proxies = {
            "ftp": params["proxy_url"],
            "http": params["proxy_url"],
            "https": params["proxy_url"],
        }
    req = requests.get(url, stream=True, proxies=proxies)
    headers = {'Content-Length': req.headers['Content-Length']}
    return Response(
        stream_with_context(req.iter_content(chunk_size=CHUNK_SIZE)),
        content_type=req.headers.get('Content-Type',
                                     'application/octet-stream'),
        headers=headers)


@ipxe.route('/kernel/<uuid>')
def kernel(uuid):
    params = get_host_params(uuid)
    url = params.get('kernel')
    if url is None:
        abort(404)
    return proxy(url, params)


@ipxe.route('/initrd/<uuid>', defaults={'module_id': 0})
@ipxe.route('/initrd/<uuid>/<int:module_id>')
@ipxe.route('/module/<uuid>', defaults={'module_id': 0})
@ipxe.route('/module/<uuid>/<int:module_id>')
def module(uuid, module_id):
    params = get_host_params(uuid)
    url = params.get('module%d' % module_id)
    if url is not None:
        return proxy(url, params)
    url = params.get('module')
    if url is not None and module_id == 0:
        return proxy(url, params)
    abort(404)


@ipxe.route('/register/<uuid>')
def register(uuid):
    params = {"groups": ["default"]}
    create_host(uuid, params)
    return make_response("", 201, [])
