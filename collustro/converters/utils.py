#!/usr/bin/env python


class ConvertException(Exception):
    def __init__(self, obj, target):
        message = 'Cannot convert %s to %s' % \
                (str(obj), str(target))
        Exception.__init__(self, message)
