#!/usr/bin/env python2

# required for sys.path
# required for os.path
import os, sys

# manually add folders to the system path so we can find ATHPy
lib_path = os.path.abspath("../")
sys.path.append( lib_path )

# import our ATHPy
from ATHPy import StrUtl
from ATHPy import EnvUtl

# use our ATHPy
print( "%s" % StrUtl.isFloatString("3.14"))

# Example of how to run a simple command
os.system('ls')

# Example of how to run a command with a return value
output = EnvUtl.execute('ls')
print(output)

