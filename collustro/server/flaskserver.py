#!/usr/bin/env python
"""
setup static and template folders
Flask(static_folder, template_folder)
"""

import logging
import multiprocessing
import os
import webbrowser

import flask

# get home
home = os.path.expanduser('~')
static_folder = '%s/.collustro/static' % home
template_folder = '%s/.collustro/templates' % home


def make_server(name=None, **kwargs):
    if name is None:
        name = 'collustro'
    kwargs['static_folder'] = kwargs.get('static_folder', static_folder)
    kwargs['template_folder'] = kwargs.get('template_folder', template_folder)
    server = flask.Flask(name, **kwargs)
    return server


def run(server, async, **kwargs):
    host = kwargs.get('host', '127.0.0.1')
    port = kwargs.get('port', 5000)
    addr = 'http://%s:%i' % (host, port)
    if async:
        process = multiprocessing.Process(target=server.run, kwargs=kwargs)
        server.running = True
        server.addr = addr
        server.host = host
        server.port = port
        server.process = process
        process.start()
        webbrowser.open(addr)
        return process
    else:
        webbrowser.open(addr)
        server.run(**kwargs)


def stop(server):
    if server.running:
        server.process.terminate()
        server.process.join()
