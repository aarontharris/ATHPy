#!/usr/bin/env python2.7

# Currently supports Python 2.7.10 -- Standard OSX Distribution

# # RELPATH for tests ## WARNING: sort imports on save must be turned off :(  @SEE: PyDev->Editor->Save Actions
import os, sys
lib_path = os.path.abspath( ".." )
sys.path.append( lib_path )

from aetypes import Enum  # NOT COMPAT 3.0
from subprocess import call
from SomeSampleClasses import Square
from ATHPy import StrUtl

import sys


def method1():
    print( "method1" )

def method2():
    print( "method2" )

# take another method as an argument
def doStuff( delegate ):
    print( "doing stuff" )
    delegate()
    print( "did stuff" )

# instantiate
shape = Square()
shape.setColor( "red" )  # set to "red", False, False, None
shape.setColor( "red", True )  # set to "red", True, False, None
shape.setColor( "red", True, True )  # set to "red", True, True, None
shape.setColor( "red", True, False, params="reversed" )  # set to "red", False, True, params=reversed  -- WTF
print ( shape.describe() )



# system call
call( ["ls", "-l"] )

# dictionaries
dictionary = {
    'one' : 1,
    'two' : 2,
}
print ( "One: %s, Two: %s" % ( dictionary['one'], dictionary['two'] ) )

# pass a method as an argument
doStuff( method2 )

# an anonymous function or lambda -- lambdas are only simple one-liners
print ( "Version %r" % sys.version_info.major )
# doStuff( lambda: print( "blah" ) )  # cant lambda print in Python 2.7
# doStuff( lambda x=1: print( "slartibartfast %r" % x ) )

# overwrite a method name with another method... wtf... woah... careful
method1()
method1 = method2
method1()

# Enums !!
# from enum import Enum ### don't forget the import as our enum Color is derived from Enum
class Color( Enum ):
    red = 1
    green = 2
    blue = 3

print( "Color: %r" % Color.red )  # NOTE: Python 3+ prints the enum class, name and ordinal

# printing without newline
sys.stdout.write( "this is" )
sys.stdout.write( " on the same line" )
print( "" )

division = 5 / 2
print( "5/2   = %r" % division )

division = 5 / 2.0
print( "5/2.0 = %r" % division )

matchingSymbolString = "{.{.}.}.{.}"
matchingSymbolPos = StrUtl.findMatchingSymbol( matchingSymbolString, "{", "}" )
print( "MatchingSymbolPos: [%r]='%r'" % ( matchingSymbolPos, matchingSymbolString[matchingSymbolPos] ) )
