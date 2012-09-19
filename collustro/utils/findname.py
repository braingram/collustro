#!/usr/bin/env python

import inspect


def get_arg_name(line, index):
    s = line.strip()
    i = line.find('(')
    if i == -1:
        raise ValueError("Failed to find arg name index[%i] in %s" % \
                (index, line))
    return s[i + 1: -1].split(',')[index]


def find(frames, name, lvl):
    if lvl == 0:
        return name
    f, _, _, fn, _, _ = frames.pop(0)
    lvl -= 1
    argindex = inspect.getargspec(f.f_globals[fn]).args.index(name)
    line = inspect.getframeinfo(frames[0][0]).code_context[0].strip()
    name = get_arg_name(line, argindex)
    print name, lvl, line, argindex
    return find(frames, name, lvl)


def find_name(obj, lvl=1):
    """
    lvl : how many frames to traverse
        0 : is pointless (will just return 'obj')
        1 : gives name of obj from frame that called find_name
        >1 : further outer frames
    """
    f = inspect.currentframe()
    ofs = inspect.getouterframes(f)
    return find(ofs[:], 'obj', lvl)


def test_find_name(obj):
    return find_name(obj, lvl=2)
