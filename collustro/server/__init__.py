#!/usr/bin/env python

import dataview
import flaskserver

from .. import utils

global collustro_server
collustro_server = None


def get_global_server(**kwargs):
    global collustro_server
    if collustro_server is None:
        collustro_server = flaskserver.make_app(**kwargs)
    # register dataview
    collustro_server.dataview = dataview.DataView()
    collustro_server.dataview.add_routes(collustro_server)
    return collustro_server


def register(obj, name=None, server=None):
    if server is None:
        server = get_global_server()
    if name is None:
        name = utils.find_name(obj, lvl=2)
    server.dataview.register(obj, name)


def show(server=None, async=False, **kwargs):
    if server is None:
        server = get_global_server()
    return flaskserver.run(server, async, **kwargs)
