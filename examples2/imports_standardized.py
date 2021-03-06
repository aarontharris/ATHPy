#!/usr/bin/env python2.7

# these are not shared with scripts that import this script
import os,sys 

# lib path IS shared with scripts that iport this script
sys.path.append( os.environ.get( "ATHPYDIR", "../ATHPy/" ) )

from ATHPy import StrUtl # these are not shared in the scripts that import this script

# defined methods are shared with scripts that import this script
def someReusableMethod(): # {
    print "Hello World from someReusableMethod"
# }