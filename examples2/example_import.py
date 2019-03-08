#!/usr/bin/env python2

# required for sys.path
# required for os.path
import os, sys
import example_proper_script as eps

# manually add folders to the system path so we can find ATHPy
lib_path = os.path.abspath("../")
sys.path.append( lib_path )

# import our ATHPy
from ATHPy import StrUtl

# use our ATHPy
print( "%s" % StrUtl.isFloatString("3.14"))

eps.sampleMethod("hi")
