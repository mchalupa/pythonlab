#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import state
from ping import cmd_ping

def cmd_shutdown(msg):
    """
    Provide exit of bot. (raise SystemExit exception)

    @param msg  unused, only for consistence with other commands
    """
    cmd_ping('ping=off') # kill ping thread
    raise SystemExit

if __name__ == "__main__":

    # do a simple test
    try:
        cmd_shutdown('')
    except SystemExit:
        print("Cought a SystemExit exception, all's OK!")
        exit(0)

    # if something's wrong, we get here
    print("Error!! No SystemExit exception")
    exit(-1)
