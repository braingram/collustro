#!/usr/bin/env python

from .. import server
from .. import utils
#from .. import wrappers


def register(obj, name=None, view=None, serv=None):
    if name is None:
        name = utils.find_name(obj, lvl=2)

    # wrap object
    #wrapped = wrappers.wrap(obj)

    # setup wrapped object with server
    server.register(name, obj, view=view, serv=serv)

    #return wrapped
