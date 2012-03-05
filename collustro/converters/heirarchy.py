#!/usr/bin/env python

# for d3 layouts:
#  1) Tree
#  2) Treemap
#  3) Pack
#  4) Partition
#  5) Cluster
#  6) Heirarchy

import json

import utils


def raise_convert_error(obj):
    raise utils.ConvertException(obj, 'heirarchy')


def convert(obj):
    """
    Try to convert an object to a json heirarchy object like (from d3):
    {
      "name": "flare",
      "children": [
        {
          "name": "analytics",
          "children": [
            {"name": "AgglomerativeCluster", "size": 3938},
            {"name": "CommunityStructure", "size": 3812},
            {"name": "MergeEdge", "size": 743}
          ]
        },
        {
          "name": "graph",
          "children": [
            {"name": "BetweennessCentrality", "size": 3534},
            {"name": "LinkDistance", "size": 5731}
          ]
        }
      ]
    }
    """
    return {
        dict: from_dict,
        list: from_list,
    }.get(type(obj), raise_convert_error)(obj)


def from_dict(d):
    """
    format:
    {'main name': {children....}}

    where children are of type:
    {'name': <value or children>}
    """
    children = from_dict_to_children(d)
    if len(children) == 1:
        return json.dumps(children[0])
    else:
        # TODO make this a more informative error
        raise Exception("Invalid conversion")


def from_dict_to_children(d):
    children = []
    for k, v in d.iteritems():
        if type(v) == dict:
            children.append({'name': k, \
                    'children': from_dict_to_children(v)})
        else:
            children.append({'name': k, 'size': v})
    return children


def from_list(l):
    """
    format:
    [ [1, [2,3,4], 5] ]

    should be a list of lists with the dimension 0 len 1
    so that the main_name can be set correctly
    """
    if len(l) != 1:
        return from_dict(list_to_dict([l]))
    else:
        return from_dict(list_to_dict(l))


def list_to_dict(l, level=''):
    """
    Use a numbered heirarchy
    1, 1.1, 1.2, 1.2.1
    """
    d = {}
    for (i, v) in enumerate(l):
        nl = '%s%i' % (level, i)
        if type(v) == list:
            d[nl] = list_to_dict(v, nl + '.')
        else:
            d[nl] = v
    return d
