# ATHPy (Pronounced At - Pie)
# Junk drawer of useful tidbits I don't want to re-write
# I know throwing everything in one file isn't awesome, but portability is valuable

import logging
import os

class StrUtl:
    def findMatchingSymbol( self, string, leftSymbol, rightSymbol ):
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


class DirUtl:
    __cwd = []

    def __init__( self ):
        pass

    def pushDir( self, path ):
        """Change to the given path and push the current working directory onto the stack"""
        self.__cwd.append( os.getcwd() )
        self.chdir( path )

    def popDir( self ):
        """Pop the last path off the stack and change to it. return the popped path, may be None if stack was empty"""
        try:
            path = self.__cwd.pop()
            self.chdir( path )
            return path
        except Exception as e:
            logging.exception( "dir stack is empty" )
            return None

    def getCwd( self ):
        """Get the current working directory"""
        return os.getcwd()

    def chdir( self, path, create=False ):
        """Change to the given path, optionally create it if it doesn't exist"""
        if not self.isDir( path ):
            if not create:
                raise Exception( "path does %r not exist" % path )
            else:
                os.mkdir( path )
        os.chdir( path )

    def isFile( self, path ):
        """True if the path exists and is a file"""
        return os.path.isfile( path )

    def isDir( self, path ):
        """True if the path exists and is a dir"""
        return os.path.isdir( path )

    def exists( self, path ):
        """Check if the given path exists, false for broken symlinks"""
        return os.path.exists( path )


class EnvUtl:
    def __init__( self ):
        pass

    def getEnv( self, key, defaultVal=None ):
        return os.environ.get( key, defaultVal )

    def getEnvOrFail( self, key, failMsg=None ):
        val = self.getEnv( key )
        if val == None:
            raise Exception( failMsg )
        return val


