#!/usr/bin/env python

import json
import logging
import urllib

import dataview
import flaskserver

from .. import utils

global collustro_server
collustro_server = None


def send(obj, name, server):
    addr = server.addr + '/data'
    logging.debug("Sending %s[%s] to %s" % (name, obj, addr))
    urllib.urlopen(addr, urllib.urlencode({name: json.dumps(obj)}))


def get_global_server(**kwargs):
    global collustro_server
    if collustro_server is None:
        logging.debug("Making server with kwargs: %s" % kwargs)
        collustro_server = flaskserver.make_server(**kwargs)
        # register dataview
        collustro_server.dataview = dataview.DataView()
        collustro_server.dataview.add_routes(collustro_server)
        collustro_server.running = False
    return collustro_server


def register(obj, name=None, server=None):
    if server is None:
        server = get_global_server()
    if name is None:
        name = utils.find_name(obj, lvl=2)
    if not server.running:
        logging.debug("Registering %s: %s" % (name, obj))
        server.dataview.register(obj, name)
    else:
        logging.debug("Sending %s: %s" % (name, obj))
        send(obj, name, server)


def show(server=None, async=False, **kwargs):
    if server is None:
        server = get_global_server()
    return flaskserver.run(server, async, **kwargs)


def stop(server=None):
    if server is None:
        server = get_global_server()
    flaskserver.stop(server)
