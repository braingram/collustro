#!/usr/bin/env python

import sys

import collustro

data = {'a': 20, 'b': 50, 'c': 30}

print collustro.converters.pie.from_dict(data)

layout = 'pie'
if len(sys.argv) > 1:
    layout = sys.argv[1]

collustro.explore(data, layout, debug=True)
