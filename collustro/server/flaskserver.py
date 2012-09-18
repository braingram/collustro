#!/usr/bin/env python

import collections
import json
import multiprocessing
import os
import webbrowser

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

# definitions:
#  data = python objects
#  layout = javascript object type
#  template = web file to display a layout


class Server(object):
    def __init__(self):
        self.data = {}
        self.ptype_map = collections.defaultdict(dict)
        self.layout_map = collections.defaultdict(list)
        self.template_map = collections.defaultdict(list)
        self.templates = {}
        self.static_files = {}

    def register_type_conversion(self, ptype, layout, function):
        self.ptype_map[ptype][layout] = function
        self.layout_map[layout].append(ptype)

    def register_template(self, name, layout, filename):
        if not os.path.exists(filename):
            raise IOError("File %s does not exist" % filename)
        self.template_map[layout].append(filename)
        self.templates[name] = filename

    def register_static_file(self, name, filename):
        if not os.path.exists(filename):
            raise IOError("File %s does not exist" % filename)
        if name in self.static_files.keys():
            raise NameError("static file %s already exists %s [%s]" % \
                    (name, self.static_files[name], filename))
        self.static_files[name] = filename

    def get_templates(self, layout):
        filenames = self.template_map[layout]
        if len(filenames) == 0:
            return []
        templates = []
        for fn in filenames:
            if fn in self.templates.values():
                for (k, v) in self.templates.iteritems():
                    if v == fn:
                        templates.append(k)
                        break
        return templates

    def get_data_keys(self, layout):
        keys = []
        for ptype in self.layout_map.get(layout, []):
            for k, v in self.data.iteritems():
                if type(v) == ptype:
                    keys.append(k)
        return keys

    def get_layouts(self, data):
        return self.ptype_map.get(type(data), {}).keys()

    def convert(self, datum, layout):
        return self.ptype_map[type(datum)][layout](datum)

    def register_with_flask(self, app):
        @app.route('/template/<name>/<key>')
        def render_template(name, key):
            if key not in self.data.keys():
                flask.abort(404)
                return None  # never called

            # check if template name exists
            if name not in self.templates.keys():
                flask.abort(404)
                return None  # never called

            # get template
            filename = self.templates[name]

            s = None
            with open(filename, 'r') as f:
                s = f.read()

            if s is None:
                flask.abort(400)  # TODO sensible error
                return None  # never called

            # render template
            return flask.render_template_string(s, data_key=key)

        @app.route('/template')
        def get_template_keys():
            return json.dumps(self.templates.keys())

        @app.route('/data/<layout>/<key>')
        def get_datum(layout, key):
            if key not in self.data.keys():
                flask.abort(404)
                return None

            datum = self.data[key]
            layouts = self.get_layouts(datum)
            if layout not in layouts:
                flask.abort(400)  # TODO sensible error and logging
                return None
            try:
                return self.convert(datum, layout)
            except Exception:  # TODO convert exception
                flask.abort(400)  # TODO sensible error and logging
                return None

        @app.route('/static/<name>')
        def get_static(name):
            if name not in self.static_files.keys():
                flask.abort(404)
                return None
            s = None
            with open(self.static_files[name], 'r') as f:
                s = f.read()

            if s is None:
                flask.abort(400)
                return None

            r = flask.make_response(s)
            # TODO change response type?
            return r

        @app.route('/templates/<key>')
        def get_templates_for_datum(key):
            if key not in self.data.keys():
                flask.abort(404)
                return None

            layouts = self.get_layouts(self.data[key])
            templates = []
            for layout in layouts:
                templates += self.get_templates(layout)
            return json.dumps(templates)

        @app.route('/data/<layout>')
        def get_data_keys(layout):
            return json.dumps(self.get_data_keys(layout))

        @app.route('/data')
        def get_all_data_keys():
            return json.dumps(self.data.keys())

        @app.route('/')
        def default():
            return render_template('default', self.data.keys()[0])

        return app

    def make_flask_app(self, name):
        app = flask.Flask(name)
        self.register_with_flask(app)
        return app

    def run(self, *args, **kwargs):
        """
        if async=True, run using multiprocessing.Process and
        return the Process object. Use process.terminate and
        process.join to stop
        """
        name = kwargs.get('name', 'collustro')
        async = kwargs.get('async', False)
        app = self.make_flask_app(name)
        if async:
            server = multiprocessing.Process(target=app.run)
            server.start()
            webbrowser.open('http://127.0.0.1:5000')
            return server
        else:
            webbrowser.open('http://127.0.0.1:5000')
            app.run(*args, **kwargs)
