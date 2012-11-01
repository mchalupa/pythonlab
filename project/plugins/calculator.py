#!/usr/bin/env python
# -*- coding: utf-8 -*-

import state

def cmd_calc(inp):
    """
    Simple calculator plugin

    @param inp      input string
    """

    allowed_chars = " 0123456789+-*/()"
    par = 0;
    for i in range(0, len(inp)):
        if inp[i] not in allowed_chars:
            return state.next("Unknown syntax")
    else:   # for's else
        try:
            out = eval(inp)
        except SyntaxError:
            return state.next("Syntax error")

    return state.done(out)


def main():
    if cmd_calc('5 + 2').value != 7:
        print("Error with argument '5 + 2'")

    if cmd_calc('-1 + 0').value != -1:
        print("Error with argument '-1 + 0'")

    if cmd_calc('5').value != 5:
        print("Error with argument '5'")

    if cmd_calc('5*5').value != 25:
        print("Error with argument '25'")

    # udelat zbytek testu
    # a hlavne dodelat ten UNITS modul i pro objekty!!

    return 0

if __name__ == '__main__':
	main()

