#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import state
#import logging  # famework pro ukladani logu, je to prej drsny

# recived words
WORDSCOUNT = 0

def cmd_shutdown(msg):
    raise SystemExit

def cmd_help(msg):
    return state.done("Help messages")

def cmd_wordscount(msg):
    global WORDSCOUNT
    
    return state.done("Actual word count is: %d words" % WORDSCOUNT)

    
def filter_wordscount(msg):
    global WORDSCOUNT
    
    WORDSCOUNT += len(msg.split())
    
    return state.done(msg)

    
class IrcBot(object):
    # nedavejte do teto tridy nic jineho, nez jsme tu uvedli
    # implementace prikazu i filtru budou mimo tridu, stejne tak
    # jako jejich pripadne globalni promenne
    COMMANDS = {
                "SHUTDOWN":cmd_shutdown,
                "HELP":cmd_help,
                "word-count":cmd_wordscount
                }
                
    FILTERS = [filter_wordscount]

    def __init__(self, interface):
        self._if = interface

    def parse(self, msg):
        """
        Parse a message, return relevant output.

        @param msg: unparsed message
        @type msg: str
        @return: message to print or None (if there's no output to print)
        @rtype: str|None
        """

        # split message into first word + rest of line
        try:
            command, args  = msg.split(None, 1)
        except ValueError:
            command, args = msg, ""

        if command in self.COMMANDS:
            stat = self.COMMANDS[command](args)
            if state.is_done(stat):
                return stat.value
            else:
                return None
            
        for func in self.FILTERS:
            stat = func(msg)
            
            if state.is_done(stat):
                return stat.value
            elif state.is_replace(stat):
                msg = stat.value
        
        return msg
        
    def run(self):
        while True:
            msg = self._if.read()
            msg = self.parse(msg)
            if msg:
                self._if.write(msg)


class BotInterface(object):

    
    def __init__(self):
        pass

    def read(self):
        """
        Read input and return it.

        @return: read data
        @rtype: str
        """
        return raw_input()

    def write(self, arg):
        """
        Write (send) argument to output.

        @param arg: text to be written to the output
        @type arg: str
        """
        print(arg)





if __name__ == "__main__":
    intf = BotInterface()
    bot = IrcBot(intf)
    bot.run()
