#!/usr/bin/env python

import json
import logging

import flask

from .. import utils


class DataView(object):
    def __init__(self):
        self.data = {}

    def register(self, obj, name=None):
        if name is None:
            name = utils.find_name(obj, lvl=2)
        self.data[name] = obj

    def add_routes(self, app, prefix='/data'):
        @app.route('%s' % prefix, methods=['GET', 'POST', 'PUT'])
        def keys():
            logging.debug("DataView.keys()")
            if flask.request.method == 'GET':
                return json.dumps(self.data.keys())
            else:  # put or post
                print dir(flask.request)
                print "flask.request.args", flask.request.args
                print "flask.request.data", flask.request.data
                print "flask.request.form", flask.request.form
                print "flask.request.form.keys()", flask.request.form.keys()
                for k, v in flask.request.form.iteritems():
                    self.data[k] = json.loads(v)
                #print "as json", json.loads(flask.request.form)
                #self.data.update(flask.request.form)
                return flask.Response(status=200)

        @app.route('%s/<key>' % prefix)
        def datum(key):
            logging.debug("DataView.datum(%s)" % key)
            if (key is None) or (key == ''):
                return keys()
            if key not in self.data.keys():
                flask.abort(404)
            return json.dumps(self.data[key])

        return app


def test():
    app = flask.Flask(__name__)
    dv = DataView()
    dv.register(1, 'a')
    dv.register(2, 'b')
    app = dv.add_routes(app)
    app.run(debug=True)

if __name__ == '__main__':
    test()
