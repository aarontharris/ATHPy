#!/usr/bin/env python3

# EXAMPLE: ./example_athgetopts.py --output=asdf --ids=1,2,3

import os, sys

sys.path.append( os.environ.get( "ATHPYDIR" ) )
from ATHPy3 import AthOpts
from ATHPy3 import StrUtl

import getopt

def __main():  # {
    print("Hello World")

<<<<<<< Updated upstream
    atOpts = AthOpts()
    atOpts.add({ 'long': 'output', 'short': 'o', 'type': 'string', 'req': False, 'desc': "Output Filename", 'default': 'output.out' })
    atOpts.add({ 'long': 'verbose', 'short': 'v', 'type': 'bool', 'req': False, 'desc': "is verbose?", 'default': False })
    atOpts.add({ 'long': 'version', 'short': 'ver', 'type': 'string', 'req': False, 'desc': "version number", 'default': '1.0' })
    atOpts.add({ 'long': 'ids', 'type': 'csv', 'req': True, 'desc': "input ids required" })
    atOpts.add({ 'long': 'extra', 'type': 'csv', 'req': False, 'desc': "input ids not required", 'visible': False })
=======
    #opt = Opt('output', 'o', Typ.STRING, False, 'Output Filename', 'output.out')

    atOpts = ATOpts(False)
    atOpts.add(Opt('output', 'o', Typ.STRING, False, 'Output Filename', 'output.out').pos())
    atOpts.add(Opt('verbose', 'v', Typ.BOOL, False, "is verbose?", False))
    atOpts.add(Opt('version', 'ver', Typ.FLOAT, False, "version number", '1.0'))
    atOpts.add(Opt('ids', 'i', Typ.CSV, True, 'input ids, example required'))
    atOpts.add(Opt('extra', 'e', Typ.CSV, False, 'input ids, example not required & not visble', None, False )) # not visible
>>>>>>> Stashed changes

    if atOpts.buildSafe(sys.argv):
        print("OUTPUT : '%s'" % atOpts.get('output'))
        print("VERBOSE: '%s'" % atOpts.get('verbose'))
        print("VERSION: '%s'" % atOpts.get('version'))
        print("IDS    : '%s'" % atOpts.get('ids'))
        print("EXTRA  : '%s'" % atOpts.get('extra'))

# }

if __name__ == "__main__": __main()
