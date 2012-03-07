#!/usr/bin/env python

import sys

import collustro

data = {'flare': {
    'analytics': {
        'cluster': {
            'AgglomerativeCluster': 3938,
            'CommunityStructure': 3812,
            'MergeEdge': 743,
            },
        'graph': {
            'BetweennessCentrality': 3534,
            'LinkDistance': 5731,
            },
        },
    }}

print collustro.converters.heirarchy.from_dict(data)

layout = 'tree'
if len(sys.argv) > 1:
    layout = sys.argv[1]

collustro.explore(data, layout, debug=True)
