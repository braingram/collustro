#!/usr/bin/env python

import json

import utils

valid_types = [dict, list]


def raise_convert_error(obj):
    raise utils.ConvertException(obj, 'pie')


def convert(obj):
    """
    Try to convert an object to a json pie object like (from d3):
    data = [{"label":"one", "value":20},
        {"label":"two", "value":50},
        {"label":"three", "value":30}];
    """
    return {
        dict: from_dict,
        list: from_list,
    }.get(type(obj), raise_convert_error)(obj)


def from_dict(d):
    """
    """
    return json.dumps([{'label': k, 'value': v} for k, v in d.iteritems()])


def from_list(l):
    """
    """
    return json.dumps([{'label': str(i), 'value': v} for i, v in enumerate(l)])
