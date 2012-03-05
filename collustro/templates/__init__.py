#!/usr/bin/env python

import os


def find_template(layout):
    template_dir = os.path.join(os.path.dirname(__file__), 'defaults')
    template_filename = os.path.join(template_dir, layout + '.html')
    if not os.path.exists(template_filename):
        raise OSError("Template %s not found in %s" % \
                (layout, template_dir))
    return template_filename
