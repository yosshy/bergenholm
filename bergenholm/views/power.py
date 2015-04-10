import requests

from flask import (
    Blueprint, abort, make_response, jsonify, request
)

from bergenholm.database.hosts import get_host_params
from bergenholm import power as power_driver


power = Blueprint('power', __name__)


@power.route('/<uuid>', methods=["PUT"])
def power_change(uuid):
    try:
        host_params = get_host_params(uuid)
        if "power_driver" not in host_params:
            abort(400)
        request_params = request.get_json()
        power = request_params.get("power")
        if power == "on":
            power_driver.power_on(**host_params)
        elif power == "off":
            power_driver.power_off(**host_params)
        elif power == "reset":
            power_driver.power_reset(**host_params)
        else:
            abort(400)
        return make_response("", 202, [])
    except KeyError:
        abort(404)


@power.route('/<uuid>')
def power_status(uuid):
    try:
        params = get_host_params(uuid)
        if "power_driver" not in params:
            abort(400)
        return jsonify(power_driver.power_status(**params))
    except KeyError:
        abort(404)
