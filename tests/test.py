#!/usr/bin/env python

import sys

import collustro

heirarchy = {'flare': {
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

pie = {'a': 20, 'b': 50, 'c': 30}


#collustro.explore({'pie': pie, 'heirarchy': heirarchy}, debug=True)
collustro.explore(locals(), debug=True)
