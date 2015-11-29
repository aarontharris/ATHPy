#!/usr/bin/python

import logging
import sys
import getopt
import ATHPy
from ATHPy import GetOpts

opts = GetOpts()
try:  # {
    opts.addDescription( "Blah" )
    opts.add( "platform", "p", "string", "Which platform are we installing on" )
    opts.build( sys.argv )
    aaron = opts.get( 'aaron', 0 )
    print "aaron got '%s'" % aaron
except Exception as e:
    # logging.exception( e )
    print "Invalid Usage: %s\n" % str( e )
    print opts.usage()
# }


