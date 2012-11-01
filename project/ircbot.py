#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import plugins
import plugins.state

# rename state for compatibility
state = plugins.state

class IrcBot(object):

    def __init__(self, interface):
        self._if = interface
    COMMANDS = plugins.COMMANDS
    FILTERS = plugins.HOOKS
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
            elif state.is_next(stat):
                print(stat.value)
                return None
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
            try:
                msg = self._if.read()
            except EOFError, KeyboardInterrupt:
                print("Shutting down..")
                exit(0)

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

        return raw_input("> ")

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
