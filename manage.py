#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

from flask import Flask
from flaskext.actions import Manager
import settings
from bergenholm import app

app.config.from_object(settings)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
