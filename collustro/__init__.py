#!/usr/bin/env python

from server import register, show

__all__ = ['register', 'show', 'explore']


def explore(data, **kwargs):
    assert isinstance(data, dict)
    [register(v, k) for k, v in data.iteritems()]
    show(**kwargs)
