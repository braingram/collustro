#!/usr/bin/env python

import flaskserver

# this is the default
from flaskserver import Server

__all__ = ['flaskserver', 'Server']

global serv
serv = None


def register(name, obj, view=None, serv=None):
    if serv is None:
        serv = get_global_server()
    serv.register(name, obj, view)


def get_global_server():
    global serv
    if serv is None:
        serv = Server()
    return serv


def show(*args, **kwargs):
    if 'serv' in kwargs:
        serv = kwargs.pop('serv')
    else:
        serv = get_global_server()
    [register(
    serv.run(**kwargs)
