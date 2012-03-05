#!/usr/bin/env python

import converters
import server
import templates

__all__ = ['converters', 'server', 'templates']


structure_map = {
        'tree': converters.heirarchy.convert,
        'treemap': converters.heirarchy.convert,
        'pack': converters.heirarchy.convert,
        'bubble': converters.heirarchy.convert,
        'partition': converters.heirarchy.convert,
        'cluster': converters.heirarchy.convert,
        }


def raise_structure_map_error(layout):
    raise Exception("Unknown layout: %s" % layout)


def explore(obj, layout, *args, **kwargs):
    """
    layout lookup
    """
    # load template (from layout)
    template_filename = templates.find_template(layout)

    # convert object to correct structure (from layout)
    data = structure_map.get(layout, raise_structure_map_error)(obj)

    # serve it all up
    app = server.render_data(template_filename, data)

    app.run(*args, **kwargs)
