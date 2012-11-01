#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state

# recived words
WORDSCOUNT = 0

def cmd_wordscount(msg):
    """
    Return actual word count

    @param msg      unused, only for keeping consistecy with other
                    commands
    """

    global WORDSCOUNT

    return state.done("Actual word count is: %d words" % WORDSCOUNT)

def filter_wordscount(msg):
    """
    Count words in input message.

    @param msg      input message
    """

    global WORDSCOUNT

    WORDSCOUNT += len(msg.split())

    return state.done(msg)


#DO SOME UNITS
