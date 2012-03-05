#!/usr/bin/env python

import os

import flask


def render_data(template_filename, data):
    template_dir, template_name = os.path.split(template_filename)
    app = flask.Flask(__name__, template_folder=template_dir)

    @app.route('/')
    def render():
        return flask.render_template(template_name)

    @app.route('/data')
    def get_data():
        return data

    return app
