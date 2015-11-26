#!/usr/bin/env python2.7

# # RELPATH for tests ## WARNING: sort imports on save must be turned off :(  @SEE: PyDev->Editor->Save Actions
import os, sys
lib_path = os.path.abspath( ".." )
sys.path.append( lib_path )

from aetypes import Enum  # NOT COMPAT 3.0
from subprocess import call
from SomeSampleClasses import Square
from ATHPy import StrUtl

import sys

value = None
print( "isString(%r)='%r'" % ( value, StrUtl.isString( value ) ) )

value = "Hello"
print( "isString(%r)='%r'" % ( value, StrUtl.isString( value ) ) )

value = "3.141592653589792"
print( "isString(%r)='%r'" % ( value, StrUtl.isString( value ) ) )

value = None
print( "isNumberString(%r)='%r'" % ( value, StrUtl.isNumberString( value ) ) )

value = "3.141592653589792"
print( "isNumberString(%r)='%r'" % ( value, StrUtl.isNumberString( value ) ) )

value = 3.141592653589792
print( "isNumberString(%r)='%r'" % ( value, StrUtl.isNumberString( value ) ) )

value = 3
print( "isNumberString(%r)='%r'" % ( value, StrUtl.isNumberString( value ) ) )

value = -3
print( "isNumberString(%r)='%r'" % ( value, StrUtl.isNumberString( value ) ) )

value = 0
print( "isNumberString(%r)='%r'" % ( value, StrUtl.isNumberString( value ) ) )

value = None
print( "isFloat(%r)='%r'" % ( value, StrUtl.isFloat( value ) ) )

value = "3.141592653589792"
print( "isFloat(%r)='%r'" % ( value, StrUtl.isFloat( value ) ) )

value = 3.141592653589792
print( "isFloat(%r)='%r'" % ( value, StrUtl.isFloat( value ) ) )

value = 3
print( "isFloat(%r)='%r'" % ( value, StrUtl.isFloat( value ) ) )

value = -3
print( "isFloat(%r)='%r'" % ( value, StrUtl.isFloat( value ) ) )

value = 0
print( "isFloat(%r)='%r'" % ( value, StrUtl.isFloat( value ) ) )

