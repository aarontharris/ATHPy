# ATHPy (Pronounced At - Pie)
# Junk drawer of useful tidbits I don't want to re-write
# I know throwing everything in one file isn't awesome, but portability is valuable

import shutil
import logging
import os
import subprocess
import getopt
#import re # Regular Expression
import sys
import re
import __main__ as main
from sys import platform as _platform



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
def doc( *line ):
    def annotate( function ):
        return function
    return annotate


# Log #########################
class Log:  # {
    @staticmethod
    def __msg( msg, _error=False, _newline=True ):  # {
        writeMe = str( msg )
        if _newline:
            writeMe += "\n"
        if _error:
            sys.stderr.write( writeMe )
        else:
            sys.stdout.write( writeMe )
    # }

    @staticmethod
    def d( msg, newline=True ):  # {
        Log.__msg( msg, _error=False, _newline=newline )
    # }

    @staticmethod
    def e( *obj ):  # {
        for o in obj:
            if isinstance( o, Exception ):
                logging.exception( o )
            else: # if isinstance( o, basestring ):
                Log.__msg( o, _error=True, _newline=True )
    # }

    @staticmethod
    def eMsg( exception ):  # {
        Log.__msg( str( exception ), _error=True, _newline=True )
    # }
# }

class AthOpts: # {
    __optDefs = {} # dict<key, dict> of key => argument definitions, key is based on 'long' key
    __validDefs = ['long','short','type','req','desc','lamda','visible','default']
    __values = {} # dict<key, value> of key => cmdline argument, key is based on 'long' key
    __validTypes = ['bool', 'int', 'float', 'string', 'csv']

    def __init__(self): # {
        pass
    # }

    @doc() # Overrides if key is already present
    @doc() # key is based on 'long' if present else 'short'
    @throws( Exception ) # when 'long' nor 'short' are present
    def add( self, argDef ): # {
        self.__validateDef(argDef) # ensures 'long' is present
        self.__optDefs[argDef['long']] = argDef
    # }

    @doc() # obtain a value associated with the given 'long' *key* based on default rules
    @params( key=str ) # based on the 'long' key provided in add()
    @output( any ) # type depends on type described in the provided argDef in add()
    def get( self, key ): # {
        if key in self.__values:
            return self.__values.get(key)
        if key not in self.__optDefs:
            raise Exception("ERR: '%s' - Unrecognized param" % key)
        argDef = self.__optDefs.get(key)
        return argDef.get('default', None)
    # }

    @throws( Exception ) # when invalid
    def __validateDef( self, argDef ): # {
        for key in argDef:
            if key not in self.__validDefs:
                raise Exception("Invalid argDef param '%s' @ '%s'" % (key, argDef.get('long')))

        if 'long' not in argDef and 'short' not in argDef:
            raise Exception("ERR: Required argDef 'long' and/or 'short'")

        if 'type' not in argDef:
            raise Exception("ERR: Required argDef 'type'")
        typ = argDef.get('type', None)
        if typ not in self.__validTypes:
            raise Exception("ERR: '%s' - Unrecognized type @ '%s'" % (typ, key))
        
        if 'long' not in argDef:
            argDef['long'] = argDef['short']
    # }

    def build( self, sysArgs ): # {
        for arg in sysArgs[1:]: # {
            if not arg.startswith('--'):
                raise Exception("ERR: '%s' - Arguments are preceeded with '--'" % arg)

            arg = arg[2:] # chop off leading '--'
            key, val = StrUtl.splitFirst(arg, '=')

            if key not in self.__optDefs:
                raise Exception("ERR: '%s' - Unrecognized param" % key)
            argDef = self.__optDefs.get(key)

            typ = argDef.get('type')
            if typ == 'bool':
                if StrUtl.toLower(val) == 'false':
                    self.__values[key]=False
                else:
                    self.__values[key]=True
            if typ == 'csv':
                if val == None:
                    val = argDef.get('default', None)
                if val != None:
                    val = val.split(',')
                self.__values[key]=val
            else:
                if val == None:
                    val = argDef.get('default', None)
                self.__values[key]=val
        # }

        for key in self.__optDefs:
            argDef = self.__optDefs.get(key)
            if argDef.get('req', False):
                if self.__values.get(key, None) == None:
                    raise Exception("ERR: '%s' - Required param" % key)
    # }

    @doc()  # exactly like build() except if anything goes wrong it automatically shows usage()
    @params( argv=list )  # generally sys.argv
    @output( bool )  # true if everything went well, false if there was an arg parse problem
    def buildSafe( self, argv ):  # {
        try:  # {
            self.build(argv)
            return True
        except Exception as err:
            pass
            print ("Invalid Usage: %s\n" % str( err ).rstrip())
            print (self.usage())
        # }
        return False
    # }

    def usage( self ): # {
        output = "Usage:\n"
        for key in self.__optDefs:
            argDef = self.__optDefs.get(key)
            if not argDef.get('visible', True):
                continue
            line = " --%s = [%s] %s\n" % (argDef['long'], argDef['type'], argDef['desc'])
            output = output + line
        return output
    # }

# }

# DirUtl #########################
class DirUtl:  # {
    __cwd = []

    def __init__( self ):
        pass

    @doc()  # Change to the given path and push the current working directory onto the stack
    @params( path=str )
    def pushDir( self, path ):
        self.__cwd.append( os.getcwd() )
        self.chdir( path )

    @doc()  # Pop the last path off the stack and change to it. return the popped path, may be None if stack was empty
    @output( str )  # or None if not found
    def popDir( self ):
        try:
            path = self.__cwd.pop()
            self.chdir( path )
            return path
        except Exception as e:  # @UnusedVariable
            logging.exception( "dir stack is empty" )
            return None

    @doc()  # Get the current working directory"""
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

    # @doc  # Check if the given path exists, false for broken symlinks
    @params( path=str )  # path to be checked
    @output( bool )
    @staticmethod
    def exists( path ):
        return os.path.exists( path )

    @staticmethod
    def copyFile( srcFile, dstFolder ):  # {
        if not DirUtl.exists( srcFile ):
            raise IOError( "ERROR: srcFile '%s' does not exist" % srcFile )
        if not DirUtl.exists( dstFolder ):
            raise IOError( "ERROR: dstFolder '%s' does not exist" % dstFolder )
        shutil.copy( srcFile, dstFolder )
    # }
# }


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

    @staticmethod
    def empty():
        return ""

    @staticmethod
    def isEmpty( string ):
        if ( string is None ): return True
        if ( len(string) == 0 ): return True
        return False

    @staticmethod
    def startsWith( string, value ):
        if ( string is None ): return False
        return string.startswith( value )
    
    @doc() # Return the number of times $value occurs at the beginning of $string
    @staticmethod
    def startsWithCount( string, value ):
        count = 0
        start = 0
        end = len(string)
        vlen = len(value)
        while ( start+vlen <= end and string[start:start+vlen] == value ):
            count += 1
            start += vlen
        return count

    @staticmethod
    def substrto( string, pattern, start=0, end=-1 ): # {
        if ( end == -1 ): end = len(string)
        index = string.find( pattern, start, end )
        if ( index >= 0 ):
            return string[start:index]
        return None
    # }

    @staticmethod
    def repeat( string, times ): # {
        out = ''
        for i in range(times):
            out = out + string
        return out
    # }

    @staticmethod
    def toLower( string ):
        if string:
            return string.lower()
        return None

    @staticmethod
    def toUpper( string ):
        if string:
            return string.upper()
        return None

    @doc()  # See also: string.rstrip() or string.lstrip() to remove all whitespace from ends
    @staticmethod
    def chomp( string ):
        if string:
            if string.endswith('\n'):
                return string[:-1]
            if string.endswith('\r\n'):
                return string[:-2]
        return string

    @staticmethod
    def contains( pattern, string ): # {
        if ( string ):
            return re.search( pattern, string )
        return False
    # }

    @staticmethod
    def containsci( pattern, string ): # {
        if ( string ):
            return re.search( pattern, string, re.IGNORECASE )
        return False
    # }

    @doc()  # strip left and right side whitespace
    @staticmethod
    def strip( string ):
        return StrUtl.lstrip( StrUtl.rstrip( string ) )

    @doc()  # static nullsafe version of string.lstrip()
    @staticmethod
    def lstrip( string ):
        if string: return string.lstrip()
        return string

    @doc()  # static nullsafe version of string.rstrip()
    @staticmethod
    def rstrip( string ):
        if string: return string.rstrip()
        return string

    @params( value=str )  # value to be parsed
    @output( None )
    @staticmethod
    def parseNumeric( value ):
        pass

    @doc()  # true if the given value isinstance of basestring
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
    def join( delim, joinlist ):  # {
        d = str( delim if delim else "" )
        return d.join( joinlist )
    # }

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
        except Exception as e:  # @UnusedVariable
            return -1

    @staticmethod
    def splitFirst( string, delimiter ): # {
        left = string
        right = None
        if delimiter in string:
            idx = string.index(delimiter)
            left = string[0:idx]
            right = string[idx+1:]
        return [left,right]
    # }

    @staticmethod
    def capitalize( string ):
        if len(string) == 1:
            return StrUtl.toUpper(string)
        else:
            return StrUtl.toUpper(string[0:1]) + string[1:]
    # }

    @staticmethod
    def snakeToCamel( string ): # {
        if string is None:
            return ""

        result = ""
        parts = string.split("_")
        for i in range(len(parts)):
            part = parts[i]
            if i > 0:
                part = StrUtl.capitalize(part)
            result = result + part
        return result
    # }


# EnvUtl #########################
class EnvUtl:  # {
    @staticmethod
    def isLinux():
        return _platform == "linux" or _platform == "linux2"

    @staticmethod
    def isDarwin():
        return _platform == "darwin"

    @staticmethod
    def isCygwin():
        return _platform == "cygwin"

    @staticmethod
    def isWin32():
        return _platform == "win32"

    @doc()  # Currently: Linux or Darwin
    @staticmethod
    def isUnixLike():
        return EnvUtl.isLinux() or EnvUtl.isDarwin()

    @staticmethod
    def isWin32OrCygwin():
        return EnvUtl.isWin32() or EnvUtl.isCygwin()

    @staticmethod
    def getEnv( key, defaultVal=None ):
        return os.environ.get( key, defaultVal )

    @staticmethod
    def getEnvOrFail( key, failMsg=None ):
        val = EnvUtl.getEnv( key )
        if val == None:
            raise Exception( failMsg )
        return val

    @staticmethod
    def execute( cmd ):  # {
        proc = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell=True )
        ( out, err ) = proc.communicate() # @UnusedVariable
        return out.decode('utf-8') # out will be <class 'bytes'> by default -- convert to string
    # }

    @doc()  # returns the best dir in python's lib path
    @doc()  # prefers site-packages over dist-packages
    @doc()  # worst case, returns the absolute path of the current working dir
    @staticmethod
    def getBestPythonLibDir():  # {
        for path in sys.path:
            if str( path ).endswith( "site-packages" ):
                return path
        for path in sys.path:
            if str( path ).endswith( "dist-packages" ):
                return path
        return sys.path[-1]
    # }
# }



# JsonUtl #########################
class JsonUtl:
    @staticmethod
    def __needsQuotes( value ):
        if StrUtl.isNumberString( value ):
            return False
        if StrUtl.isString( value ) and ( value == "true" or value == "false" ) :
            return False
        return True

class FileReader: # {
    __filepath = ''
    __lineNo = 0
    __callback = None
    __line = None
    __state = None
    __stop = False

    @doc()  # Read a file line by line and process the line in the given callback
    @params( filepath=str )  # the path to the file to read, arg1 passed to the callback
    @params( callback="lambda")  # "bool callback( FileReader )" called for each line. True=continue, False=stop reading file.
    def __init__( self, filepath, callback ): # {
        self.__filepath = filepath
        self.__callback = callback
        self.__state = dict()
        pass
    # }

    @doc() # Stop the line by line read
    @doc() # odd but we do this for better lambda compat
    def stop( self ): # {
        __stop = True
    # }

    def readLineByLine( self ): # {
        self.__stop = False
        self.__lineNo = 0
        with open( self.__filepath ) as fh:
            self.__line = fh.readline()
            while self.__line:
                self.__lineNo += 1
                self.__line = StrUtl.rstrip(self.__line)
                self.__callback( self )
                if self.__stop: break
                self.__line = fh.readline()
    # }

    @doc() # mutable dictionary for keeping state during traversals
    def getState( self, key, defaultVal=None ):
        return self.__state.get(key, defaultVal)

    def setState( self, key, value ):
        self.__state[key]=value
        return self

    def getLineNo( self ): return self.__lineNo
    def getLine( self ): return self.__line
# }

# FileUtl #########################
class FileUtl: # {

    @staticmethod
    def writelines( filepath, lines ): # {
        with open( filepath, 'w' ) as fh:
            for line in lines:
                fh.write(line + "\n")
    # }

    @params( chomp=bool ) # true will remove the newline char from the line
    @staticmethod
    def readAllLinesIntoArray( filepath, chomp=False ):
        with open( filepath ) as fh:
            lines = fh.readlines()
        if chomp:
            for i in range(len(lines)):
                lines[i] = StrUtl.chomp(lines[i])
        return lines

    @doc()  # Read a file line by line and process the line in the given callback
    @params( filepath=str )  # the path to the file to read, arg1 passed to the callback
    @params( method="method")  # "def methodName( filepath, state, line )" called for each line
    @params( state=object )  # an optional state object passed to the callback for each line
    @output( None )
    @staticmethod
    def readLineByLine( filepath, methodLine, state=None ): # {
        lineNo = 0
        with open( filepath ) as fh:
            line = fh.readline()
            while line:
                lineNo += 1
                line = StrUtl.rstrip(line)
                methodLine( filepath, line, state )
                line = fh.readline()
    # }
# }

@doc() # WORK IN PROGRESS
class UserState: # {
    __state = {} # key value pairs of

    @output( str ) # Whatever was previously associated with this key or None
    def put(self, key, value): # {
        prev = None
        if key in self.__state:
            prev = self.get(key, None)
        self.__state[key] = value
        return prev
    # }

    def get(self, key, defaultVal=None): # {
        return self.__state.get(key, defaultVal)
    # }

    def read(self): # {
        pass
    # }

    def write(self): # {
        pass
    # }
# }

# MavenDescriptor #########################
class MavenDescriptor:
    __groupId = None
    __artifact = None
    __version = None
    __packaging = None

    def __init__( self, groupId, artifactId, version, packaging='jar' ):  # {
        self.__groupId = groupId
        self.__artifact = artifactId
        self.__version = version
        self.__packaging = packaging
    # }

"""
my $groupId = 'com.leap12.databuddy';
my $artifact = 'DataBuddy';
my $version = '0.0.1-SNAPSHOT';
my $packaging = 'jar';
my $pathToFile = `ls target/DataBuddy*.jar`;
chomp($pathToFile);

#mvn install:install-file -Dfile=<path-to-file> -DgroupId=<group-id> -DartifactId=<artifact-id> -Dversion=<version> -Dpackaging=<packaging>
my $cmd = sprintf( "mvn install:install-file -Dfile=%s -DgroupId=%s -DartifactId=%s -Dversion=%s -Dpackaging=%s",
            $pathToFile, $groupId, $artifact, $version, $packaging
            );

#print $cmd . "\n";
system( $cmd );
"""

if __name__ == "__main__": pass
