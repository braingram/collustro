#!/usr/bin/env python

import converters
import server
import templates
import webbrowser

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
    serv.register_type_conversion(list, 'bundle', converters.bundle.convert)

    # register templates
    defaults = templates.get_defaults()
    for n, l, fn in defaults:
        serv.register_template(n, l, fn)

    if 'name' not in kwargs.keys():
        kwargs['name'] = __name__
    return serv.run(*args, **kwargs)
