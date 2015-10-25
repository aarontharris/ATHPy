#!/usr/bin/env python3.5
# /usr/bin/env python2.7
# /usr/bin/python

# from enum import Enum # 3.0+
from aetypes import Enum  # 2.7
from subprocess import call
import sys

from SomeSampleClasses import Square

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
# doStuff( lambda: print( "blah" ) )  # But not in Python 2.7.10 :(
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

print( "Color: %r" % Color.red )