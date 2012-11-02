#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state

# karma dict
KARMA = dict()

def cmd_karma(msg):
    """
    Karma command. Return string with karma of detected nick.

    @param msg  input string
    """

    global KARMA
    msg = msg.strip()
    
    if msg == '':
        return state.next('No name given')
    
    if KARMA.has_key(msg):
        return state.done(msg + "'s karma is " + str(KARMA[msg]))
    else:
        return state.done(msg + " has no karma")


def _karma_change(name, op):
    """
    Change one's karma. Should be used only by karma filter, not user.

    @param name     name to operate with
    @param op       action

    If op == ++ then increase karma by 1
    if op == -- then decrease karma by 1
    else raise ValueError. This would be critical, because op is given
    by programator --> error in program, not in user input.
    """

    global KARMA

    try:
        if op == '++':
            KARMA[name] += 1
        elif op == '--':
            KARMA[name] -= 1
        else:
            raise ValueError   # critical error (in source, not in user)
    except KeyError:
        KARMA[name] = 1 if op == '++' else -1

def filter_karma(msg):
    """
    Implement karma filter. Try catch karma commands and do appropriate
    action

    @param msg      input string
    """

    if msg.endswith('++') or msg.endswith('--'):
        # 'C++' exclusive
        if msg.lower() != 'c++' and msg[:-2].isalnum():
            _karma_change(msg[:-2], msg[-2:])
            return state.done(None)
        else:
            return state.next(msg)


# CREATE SOME UNITS
