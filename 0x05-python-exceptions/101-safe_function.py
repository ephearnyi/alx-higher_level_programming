#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        trial = fct(*args)
        return (trial)
    except:
        print("Exception: {}".format(sys.exc_info()[i]), file=sys.stderr)
        return (None)
