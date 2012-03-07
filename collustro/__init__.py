#!/usr/bin/env python

import converters
import server
import templates

__all__ = ['converters', 'server', 'templates']


import flask


def explore(data_dict, *args, **kwargs):
    """
    layout lookup
    """

    serv = server.Server()

    # set data
    serv.data = data_dict

    # register conversions
    serv.register_type_conversion(dict, 'heirarchy', \
            converters.heirarchy.convert)
    serv.register_type_conversion(list, 'heirarchy', \
            converters.heirarchy.convert)
    serv.register_type_conversion(dict, 'pie', converters.pie.convert)
    serv.register_type_conversion(list, 'pie', converters.pie.convert)

    # register templates
    defaults = templates.get_defaults()
    for n, l, fn in defaults:
        serv.register_template(n, l, fn)

    app = flask.Flask(__name__)
    serv.register_with_flask(app)

    app.run(*args, **kwargs)
