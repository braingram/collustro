#!/usr/bin/env python

from server import get_global_server, register, show

__all__ = ['get_global_server', 'register', 'send', 'show', 'explore']


def explore(data, **kwargs):
    assert isinstance(data, dict)
    [register(v, k) for k, v in data.iteritems()]
    return show(**kwargs)
