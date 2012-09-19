#!/usr/bin/env python

import logging
logging.basicConfig(level=logging.DEBUG)

import collustro

flare = {'flare': {
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

abc = {'a': 20, 'b': 50, 'c': 30}

simpsons = [{'name': 'abe', 'size': 80, 'imports': ['herb', 'homer']},
        {'name': 'mona', 'size': 80, 'imports': ['herb', 'homer']},
        {'name': 'herb', 'size': 40, 'imports': []},
        {'name': 'homer', 'size': 40, 'imports': ['bart', 'lisa', 'maggie']},
        {'name': 'clancy', 'size': 80, 'imports': ['marge', 'patty', 'selma']},
        {'name': 'jackie', 'size': 80, 'imports': ['marge', 'patty', 'selma']},
        {'name': 'marge', 'size': 40, 'imports': ['bart', 'lisa', 'maggie']},
        {'name': 'patty', 'size': 40, 'imports': []},
        {'name': 'selma', 'size': 40, 'imports': ['ling']},
        {'name': 'bart', 'size': 20, 'imports': []},
        {'name': 'lisa', 'size': 20, 'imports': []},
        {'name': 'maggie', 'size': 20, 'imports': []},
        {'name': 'ling', 'size': 20, 'imports': []}]

p = collustro.explore(locals(), debug=True)
#p = collustro.explore(locals(), debug=True, async=True)
#server = collustro.get_global_server()
#print "Data:", server.dataview.data
#print "running asynchronously: %s" % p
#c = raw_input('press enter to stop')
#p.terminate()
#p.join()
