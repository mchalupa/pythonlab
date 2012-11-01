#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state

def filter_strip(msg):
    return state.replace(msg.strip())

if __name__ == "__main__":

    if filter_strip("         strip me      ").value != "strip me":
        print("Error in strip filter input '     sth    '")

    if filter_strip("strip me      ").value != "strip me":
        print("Error in strip filter input 'sth    '")

    if filter_strip("         strip me").value != "strip me":
        print("Error in strip filter input '     sth'")
