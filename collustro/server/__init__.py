#!/usr/bin/env python

import os

import flask

# API
# 1) get layout (cluster)
# 2) get data as form
# 3) available layouts
# 4) available data
# 5) get compatible forms for data

# serve up static files
# 1) default
# 2) home
# 3) local

# js files that render a data of form into a div
# generic css files
# figure saving


def render_data(template_filename, data):
    template_dir, template_name = os.path.split(template_filename)
    default_template = os.path.splitext(template_name)[0]
    app = flask.Flask(__name__, template_folder=template_dir)

    @app.route('/')
    def render_default():
        return flask.render_template(default_template + '.html')

    @app.route('/view/<view_name>')
    def render(view_name):
        return flask.render_template(view_name + '.html')

    @app.route('/data')
    def get_data():
        return data

    return app
