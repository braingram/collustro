#!/usr/bin/env python
"""
Wrap an object adding an onchange callback
"""

global wtypes
wtypes = {}
wtypes['__default__'] = dumb_wrap


def wrap(obj, wtype=None):
    if wtype is None:
        wtype = type(obj)
    if wtype in wtypes:
        return wtypes[wtype](obj)
    return wtypes['__default__'](obj)


class Wrap(object):
    def __init__(self, obj):
        self.__raw__ = obj
        self.__sclass__ = type(obj)

    def __onchange__(self):
        pass

    def __getattribute__(self, name):
        pass


class NotifyDict(dict):
    __slots__ = ["callback"]

    def __init__(self, *args, **kwargs):
        self.callback = lambda self: None
        dict.__init__(self, *args, **kwargs)

    def _wrap(method):
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            self.callback()
            return result
        return wrapper
    __delitem__ = _wrap(dict.__delitem__)
    __setitem__ = _wrap(dict.__setitem__)
    clear = _wrap(dict.clear)
    pop = _wrap(dict.pop)
    popitem = _wrap(dict.popitem)
    setdefault = _wrap(dict.setdefault)
    update = _wrap(dict.update)


def dumb_wrap(obj):
    return Wrap(obj)
