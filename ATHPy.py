# ATHPy (Pronounced At - Pie)
# Junk drawer of useful tidbits I don't want to re-write
# I know throwing everything in one file isn't awesome, but portability is valuable

import logging
import os
import re



# Annotations #####################
def params( *types, **named ):
    def annotate( function ):
        return function
    return annotate
def output( typ ):
    def annotate( function ):
        return function
    return annotate
def see( typ ):
    def annotate( function ):
        return function
    return annotate
def throws( typ ):
    def annotate( function ):
        return function
    return annotate
def doc( line ):
    def annotate( function ):
        return function
    return annotate



# DirUtl #########################
class DirUtl:
    __cwd = []

    def __init__( self ):
        pass

    @doc  # Change to the given path and push the current working directory onto the stack
    @params( path=str )
    def pushDir( self, path ):
        self.__cwd.append( os.getcwd() )
        self.chdir( path )

    @doc  # Pop the last path off the stack and change to it. return the popped path, may be None if stack was empty
    @output( str )  # or None if not found
    def popDir( self ):
        try:
            path = self.__cwd.pop()
            self.chdir( path )
            return path
        except Exception as e:
            logging.exception( "dir stack is empty" )
            return None

    @doc  # Get the current working directory"""
    @output( str )
    def getCwd( self ):
        return os.getcwd()

    @params( path=str )  # path to be checked or created
    @params( create=bool )  # True = Will create folder if it does not exist
    @output( None )
    def chdir( self, path, create=False ):
        """Change to the given path, optionally create it if it doesn't exist"""
        if not self.isDir( path ):
            if not create:
                raise Exception( "path does %r not exist" % path )
            else:
                os.mkdir( path )
        os.chdir( path )

    @params( path=str )  # path to be checked
    @output( bool )
    def isFile( self, path ):
        """True if the path exists and is a file"""
        return os.path.isfile( path )

    @params( path=str )  # path to be checked
    @output( bool )
    def isDir( self, path ):
        """True if the path exists and is a dir"""
        return os.path.isdir( path )

    @params( path=str )  # path to be checked
    @output( bool )
    def exists( self, path ):
        """Check if the given path exists, false for broken symlinks"""
        return os.path.exists( path )



# StrUtl #########################
class StrUtl:
    # __INSTANCE__ = None
    # @staticmethod
    # def get():
    #    if StrUtl.__INSTANCE__ == None:
    #        __INSTANCE__ = StrUtl()
    #    return __INSTANCE__

    def __init__( self ):
        pass

    @params( value=str )  # value to be parsed
    @output( None )
    @staticmethod
    def parseNumeric( value ):
        pass

    @staticmethod
    def isString( value ):
        return isinstance( value, basestring )

    @staticmethod
    def isNumberString( value ):
        return StrUtl.isFloatString( value )

    @staticmethod
    def isFloatString( value ):
        # return isFloat( value ) or isInt( value ) or isLong( value )
        try:
            _ = float( value )
        except Exception:
            return False
        return True

    @staticmethod
    def isFloat( value ):
        return isinstance( value, float )

    @staticmethod
    def isInt( value ):
        return isinstance( value, int )

    @staticmethod
    def isLong( value ):
        return isinstance( value, long )

    @staticmethod
    def findMatchingSymbol( string, leftSymbol, rightSymbol ):
        try:
            """
            obeys nesting
            assumes we're reading left to right
            assumes the first character is the left symbol
            assumes left symbol and right symbol are different
            returns position of matching symbol 
            """
            l = leftSymbol
            r = rightSymbol
            pos = 0
            lCount = 1
            while lCount > 0:
                rpos = string.index( r, pos + 1 )
                lpos = string.index( l, pos + 1 )
                if lpos != -1 and lpos < rpos:
                    lCount += 1
                    pos = lpos
                else:
                    lCount -= 1
                    pos = rpos

                if pos == -1:
                    break

            return pos
        except Exception as e:
            return -1



# EnvUtl #########################
class EnvUtl:
    @staticmethod
    def getEnv( key, defaultVal=None ):
        return os.environ.get( key, defaultVal )

    @staticmethod
    def getEnvOrFail( key, failMsg=None ):
        val = EnvUtl.getEnv( key )
        if val == None:
            raise Exception( failMsg )
        return val



# JsonUtl #########################
class JsonUtl:
    @staticmethod
    def __needsQuotes( value ):
        if StrUtl.get().isNumberString( value ):
            return False
        if StrUtl.get().isString( value ) and ( value == "true" or value == "false" ) :
            return False
        return True


