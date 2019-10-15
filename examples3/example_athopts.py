#!/usr/bin/env python3

# EXAMPLE: ./example_athgetopts.py --output=asdf --ids=1,2,3

import os, sys

sys.path.append( os.environ.get( "ATHPYDIR" ) )
from ATOpts import *

def __main():  # {
    print("Hello World")

    atOpts = ATOpts(False)
    atOpts.add(Opt('output', 'o', Typ.STRING, False, 'Output Filename', 'output.out').pos())
    atOpts.add(Opt('verbose', 'v', Typ.BOOL, False, "is verbose?", False))
    atOpts.add(Opt('version', 'ver', Typ.FLOAT, False, "version number", '1.0'))
    atOpts.add(Opt('ids', 'i', Typ.CSV, True, 'input ids, example required'))
    atOpts.add(Opt('extra', 'e', Typ.CSV, False, 'input ids, example not required & not visble', None, False )) # not visible

    if atOpts.buildSafe(sys.argv):
        print("OUTPUT : '%s'" % atOpts.get('output'))
        print("VERBOSE: '%s'" % atOpts.get('verbose'))
        print("VERSION: '%s'" % atOpts.get('version'))
        print("IDS    : '%s'" % atOpts.get('ids'))
        print("EXTRA  : '%s'" % atOpts.get('extra'))

# }

if __name__ == "__main__": __main()
