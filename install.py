#!/usr/bin/python

import logging
import sys
import getopt
import ATHPy
from ATHPy import GetOpts

def main():  # {
    opts = GetOpts()
    opts.addDescription( "blah blah" )
#     opts.addDescription( "Blah2" )
    opts.add( "platform", "p", "string", True, "Which platform are we installing on", method=handlePlatform )
    opts.add( "test", "t", None, True, "testing 123", method=handleTest )

    if opts.buildSafe( sys.argv ):  # {
        platform = opts.get( 'platform', 0 )
        print "platform got '%s'" % platform
    # }
# }

def handlePlatform( val ):
    print "Got %s" % val

def handleTest( val ):
    print "Got %s" % val

if __name__ == '__main__':
    main()
