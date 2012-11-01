#!/usr/bin/python

#import state
from calculator import cmd_calc
from karma import cmd_karma, filter_karma
from shutdown import cmd_shutdown
from word_count import filter_wordscount, cmd_wordscount
from commands import cmd_help
from text_filters import filter_strip

COMMANDS = {
    "=": cmd_calc,
    "calc": cmd_calc,
    "karma": cmd_karma,
    "word-count": cmd_wordscount,
    "SHUTDOWN": cmd_shutdown,
    "HELP": cmd_help
}

HOOKS = [
    filter_strip,
    filter_karma,
    filter_wordscount,
]
