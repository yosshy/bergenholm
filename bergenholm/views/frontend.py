# -*- encoding:utf-8 -*-
from flask import Blueprint

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return "Bergenholm works!"
