#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state

def cmd_help(msg):
    """
    Help message for IrcBot

    @param msg      unused, only for consistency with other commands
    """

    help_msg =\
    """
    IrcBot

    Implemented commands: help SHUTDOWN word-count karma calc
    """
    return state.done(help_msg)
