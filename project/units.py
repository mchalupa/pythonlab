#!/usr/bin/env python
# -*- coding: utf-8 -*-

NUM = 0
ERRORS = 0

def unit(return_state, func, *args):
    """
    Do a single unit test

    @param return_state     return state that shoud be returned
                            if everything is ok
    @param func             function to be tested
    @param args             arguments to the function
    """

    global ERRORS
    global NUM

    NUM += 1

    if func(*args) != return_state:
        ERRORS += 1
        print str(func), " failed with arguments: (", str(*args), ")\n"

def unit_bool(func, *args):
    """
    Do a single unit test, decide if ok acording to return value
    (in python boolean meaning)

    @param func             function to be tested
    @param args             arguments to the function
    """

    global ERRORS
    global NUM

    NUM += 1

    if not func(*args):
        ERRORS += 1
        print str(func), " false return value with arguments: (", str(*args), ")"

#~ def unit_method(state, obj, method, *args):
    #~ """
    #~ Do a single unit test on object method
#~
    #~ @param state    expected return state
    #~ @param obj      object
    #~ @param method   method to be run
    #~ @args           arguments for method
    #~ """
#~
    #~ global ERRORS
    #~ global NUM
#~
    #~ NUM += 1
#~
    #~ if state != obj.method(*args):
        #~ ERRORS += 1
        #~ print str(func), "() failed with arguments: (", str(*args), ")\n"
#~
#~ def unit_object_attr(obj, methods, attrs):
    #~ """
    #~ Run all methods on obj and then check if given attributs are
    #~ consistent
#~
    #~ @param obj      object
    #~ @param methods  list of methods to be run
    #~ @param attrs    dictionary of expected values of attributs
    #~ """
    #~ global ERRORS
    #~ global NUM
#~
    #~ NUM += 1
#~
    #~ for (method, args) in methods.items():
        #~ obj.method(args)
#~
    #~ for (attr, val) in attrs.items():
        #~ if obj.attr != val:
            #~ ERRORS += 1
            #~ print str(obj.attr), "() failed: value=",val,\
                                    #~ "expected(", str(*args), ")\n"


def unit_all(tests_list):
    """
    Perform defined unit tests

    @param tests_list       list() of unit tests to be performed
    """

    for test in tests_list:
        test()

    print ERRORS, "errors in ", NUM, " units"

def utests():
    unit(int(1), int, 1)
    unit(str('a'), str, 'a')

    unit_bool(int, 1)
    unit_bool(int, -1)



def main():
    print("Very simple unit of units ;]\n\n")

    unit(int(1), int, 1)
    unit(str('a'), str, 'a')

    unit_bool(int, 1)
    unit_bool(int, 2)

    units = list((utests, utests))

    unit_all(units)

    return 0

if __name__ == '__main__':
	main()

