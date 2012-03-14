#!/usr/bin/env python

import json

import utils

valid_types = [list]


def raise_convert_error(obj):
    raise utils.ConvertException(obj, 'bundle')


def convert(obj):
    """
    Try to convert an object to a json pie object like (from d3):
    data = [{'name': foo, 'size': 20, 'imports': []},
        {'name': bar, 'size': 10, 'imports': []}]
    """
    return {
        list: from_list,
    }.get(type(obj), raise_convert_error)(obj)


def from_list(l):
    """
    """
    if not len(l):
        return json.dumps([])

    if type(l[0]) != dict:
        raise_convert_error(l)

    if ('name' not in l[0].keys()) or ('size' not in l[0].keys()) or \
            ('imports' not in l[0].keys()):
        raise_convert_error(l)

    return json.dumps([{'name': i['name'], 'size': i['size'], \
            'imports': i['imports']} for i in l])
