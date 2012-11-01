#!/usr/bin/python

#http://www.networksorcery.com/enp/protocol/irc.htm
import re
import socket
import getpass

class IRCBotInterface(object):
    """Generic interface for working with IRC messages."""

    def read(self):
        raise NotImplemented

    def write(self, msg):
        raise NotImplemented

    def open(self):
        raise NotImplemented

    def close(self):
        raise NotImplemented


class IRCBotShellInterface(IRCBotInterface):

    def __init__(self):
        pass

    def read(self):
        return raw_input("> ")

    def write(self, msg):
        print msg

    def open(self):
        pass

    def close(self):
        pass


class IRCBotTelnetInterface(IRCBotInterface):
    def __init__(self, address = None, port = 8080):
        self._timeout = 60 * 10
        self._listen = None
        self._sfile = None
        self._socket = None

        self._addr = address
        self._port = port

    def client(self):
        return self._sfile

    def disconnected(self):
        self._socket = None
        self._sfile = None

    def read(self):
        pass

    def write(self, msg):
        pass

    def open(self):
        pass

        if self._listen == None:
            raise Exception("No valid address found")

    def close(self):
        pass

if __name__ == "__main__":
    x = IRCBotTelnetInterface("::1", 8082)
    x.open()

    while True:
        data = x.read()
        if data == "":
            break

        print "Received:", data
        x.write(data)
