#!/usr/bin/env python

import os


def get_defaults():
    template_dir = os.path.join(os.path.dirname(__file__), 'defaults')
    d = []
    for fn in ['bubble', 'cluster', 'pack', 'partition', 'tree', 'treemap']:
        filename = os.path.join(template_dir, fn) + '.html'
        d.append((fn, 'heirarchy', filename))

    filename = os.path.join(template_dir, 'pie') + '.html'
    d.append(('pie', 'pie', filename))

    filename = os.path.join(template_dir, 'bundle') + '.html'
    d.append(('bundle', 'bundle', filename))
    return d


def find_template(layout):
    template_dir = os.path.join(os.path.dirname(__file__), 'defaults')
    template_filename = os.path.join(template_dir, layout + '.html')
    if not os.path.exists(template_filename):
        raise OSError("Template %s not found in %s" % \
                (layout, template_dir))
    return template_filename
