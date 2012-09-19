#!/usr/bin/env python
"""
setup static and template folders
Flask(static_folder, template_folder)
"""

import multiprocessing
import os
import webbrowser

import flask

# get home
home = os.path.expanduser('~')
static_folder = '%s/.collustro/static' % home
template_folder = '%s/.collustro/templates' % home


def make_app(name=None, **kwargs):
    if name is None:
        name = 'collustro'
    kwargs['static_folder'] = kwargs.get('static_folder', static_folder)
    kwargs['template_folder'] = kwargs.get('template_folder', template_folder)
    app = flask.Flask(name, **kwargs)
    return app


def run(app, async, **kwargs):
    host = kwargs.get('host', '127.0.0.1')
    port = kwargs.get('port', 5000)
    addr = 'http://%s:%i' % (host, port)
    if async:
        server = multiprocessing.Process(target=app.run, kwargs=kwargs)
        app.running = True
        app.addr = addr
        app.host = host
        app.port = port
        server.start()
        webbrowser.open(addr)
        return server
    else:
        webbrowser.open(addr)
        app.run(**kwargs)
