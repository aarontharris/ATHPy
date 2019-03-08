#!/usr/bin/env python3

# Q: Why is there a .pyc file for this?
# A: Because we import this file into example_import.py
#    that causes this file to be compiles like a module

# import os, sys
# sys.path.append( os.environ.get( "ATHPYDIR" ) )
# from ATHPy3 import GetOpts

def sampleMethod( str="undef" ): # {
    print("You passed '%s'" % str)
# }

def __main(): # {
    sampleMethod("test test test")
# }

# Q: Why do we do this if __name__
# A: Because we only want to run main if THIS script was the script being run
#    rather, if we imported this script elsewhere, we don't want to run main
#    instead we just want to import the functions.
if __name__ == '__main__': __main()