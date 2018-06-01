#!/usr/bin/python

# # RELPATH for tests ## WARNING: sort imports on save must be turned off :(  @SEE: PyDev->Editor->Save Actions
import os, sys
lib_path = os.path.abspath( "./" )
sys.path.append( lib_path )

from aetypes import Enum  # NOT COMPAT 3.0
from subprocess import call
from ATHPy import StrUtl, GetOpts, EnvUtl

import logging
import sys

opts = GetOpts()
try:
    opts.add( "option", "o", "string", "sample option", True )
    opts.build( sys.argv )
    option = opts.get( "option", 0 )
    print "Option: %s" % option
except Exception as e:
    logging.exception( e )
    print "Invalid Usage: %s" % str( e )
    opts.usage()


value = 0
print( "isFloat(%r)='%r'" % ( value, StrUtl.isFloat( value ) ) )

bestLibPath = EnvUtl.getBestPythonLibDir()
print "Best Lib Path: '%s'" % bestLibPath

