# ATHPy (Pronounced At - Pie)
# Junk drawer of useful tidbits I don't want to re-write
# I know throwing everything in one file isn't awesome, but portability is valuable

import logging
import os
import subprocess
import getopt
import sys
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



# GetOpts #########################
@doc()  # Built on getopt but much more convenient
@doc()  # EX:
@doc()  # EX: import sys
@doc()  # EX: from ATHPy import GetOpts
@doc()  # EX:
@doc()  # EX: opts = GetOpts()
@doc()  # EX: opts.add("name", "n", "string", "Person's name")
@doc()  # EX: opts.add("age", "a", "int", "Person's age", method=handleAge)
@doc()  # EX: if opts.buildSafe( sys.argv ): # buildSafe shows usage() on error
@doc()  # EX:     opts.get('platform', -1)
@doc()  # EX:
@doc()  # EX: def handleAge( val ):
@doc()  # EX:     print "Age=%s" % val
@doc()  # EX:
@doc()  # EX: if __name__ == '__main__':
@doc()  # EX:     main()
@doc()  # EX:
class GetOpts:  # {
    __optData = []
    __optLookup = {}
    __optVals = {}
    __description = []
    __widest = 0
    __hasRequired = False
    __hasNotRequired = False

    def __init__( self ):  # {
        pass
    # }

    @doc()  # add accepted options
    @params( longKey=str )  # the option in long form --optionName
    @params( shortKey=str )  # the option in short form -o
    @params( opType=str )  # the expected input data type expressed to the user via usage()
    @params( req=bool )  # True if required else False or None
    @params( desc=str )  # the option description expressed to the user via usage()
    @params( public=bool )  # Display this option in the usage()
    @params( method="lambda method" )  # "def methodName( val )" even if opt takes no value. Where val = value entered by the user or None
    @output( None )
    def add( self, longKey, shortKey=None, opType=None, req=False, desc="", method=None, public=True ):  # {
        sKey = shortKey if shortKey and len( shortKey ) > 0 else "_"
        lKey = longKey if longKey and len( longKey ) > 0 else "_"
        desc = desc if desc else ""
        opType = opType if opType else ""
        opData = { "short": sKey, "long": lKey, "type": opType, "req": req, "desc": desc, "public": public, "method": method }
        self.__optData.append( opData )
        self.__optLookup[sKey] = opData
        self.__optLookup[lKey] = opData

        if req:
            self.__hasRequired = True
        if not req:
            self.__hasNotRequired = True
    # }

    @doc()  # Must be called before build() or buildSafe()
    @doc()  # The given description appears at the top of the usage
    @doc()  # Multiple descriptions can be added, each will appear in order added
    def addDescription( self, description ):
        self.__description.append( description )

    @doc()  # this or buildSafe() must be called to build and parse GetOpts
    def build( self, argv ):  # {
        shorts = []
        longs = []

        # build our getopt params, short string and long list
        # also size up the max width needed
        for opt in self.__optData:  # {
            # prefix the key with ":" or "=" if this opt requires a value
            sKey = opt['short']
            lKey = opt['long']
            if opt['type']:
                sKey = sKey + ":"
                lKey = lKey + "="

            # add to the short and long lists
            shorts.append( sKey )
            longs.append( lKey )

            # size up the max width needed
            padding = 5
            sWide = len( sKey ) + len( opt['type'] ) + padding
            lWide = len( lKey ) + len( opt['type'] ) + padding
            if sWide > self.__widest:
                self.__widest = sWide
            if lWide > self.__widest:
                self.__widest = lWide
        # }

        # parse
        opts, remainder = getopt.getopt( sys.argv[1:], "".join( shorts ), longs )  # @UnusedVariable

        # process the opt pairs
        for pair in opts:  # {
            key = str( pair[0] )
            val = str( pair[1] )

            # strip off leading - or --
            if key.startswith( "--" ):
                key = key[2:]
            else:
                key = key[1:]

            # ignore proprietary "empty" token
            if "_" == key:
                continue

            # associate value to both long and short key for generic access
            opData = self.__optLookup[key]
            self.__optVals[opData['short']] = val
            self.__optVals[opData['long']] = val

            # execute any methods associated with this opt
            if opData['method']:
                opData['method']( val )
        # }
    # }

    @doc()  # exactly like build() except if anything goes wrong it automatically shows usage()
    @params( argv=list )  # generally sys.argv
    @output( bool )  # true if everything went well, false if there was an arg parse problem
    def buildSafe( self, argv ):  # {
        try:  # {
            self.build( sys.argv )
            return True
        except Exception as e:
            # logging.exception( e )
            print "Invalid Usage: %s\n" % str( e ).rstrip()
            print self.usage()
            return False
        # }
    # }

    @doc()  # get a value by key if it was entered by the user else defaultValue
    @params( key=str )  # the short or long opt name without the leading "-" or "--"
    @params( defaultValue="any" )  # the value you will be given if the key is not found
    def get( self, key, defaultValue=None ):  # {
        if self.__optVals.has_key( key ):
            return self.__optVals[key]
        return defaultValue
    # }

    @doc()  # you may call this directly or it will be called for you via buildSafe().
    @doc()  # Auto-generated usage based on the opts you configured via add()
    def usage( self ):  # {
        out = ""

        if self.__description:  # {
            for desc in self.__description:
                out += ( desc + "\n" ) if desc else ""
            out += "\n"
        # }

        for req in [True, False]:  # {
            if req and self.__hasRequired:
                out += "Required Arguments:\n"
            if not req and self.__hasNotRequired:
                out += "Optional Arguments:\n"

            for opt in self.__optData:  # {
                if opt['req'] != req:
                    continue
                if not opt['public']:
                    continue

                if opt['long'] != "_":
                    optName = opt['long']
                    optName += ( "=<" + opt['type'] + ">" ) if opt['type'] else ""
                    desc = opt['desc']
                    outLong = ( "  --%-" + str( self.__widest ) + "s%s\n" ) % ( optName, opt['desc'] )
                    out += outLong

                if opt['short'] != "_":
                    optName = opt['short']
                    optName += ( " <" + opt['type'] + ">" ) if opt['type'] else ""
                    desc = ( "Short for: --%s" % opt['long'] ) if opt['long'] and opt['long'] != "_" else opt['desc']
                    outShort = ( "   -%-" + str( self.__widest ) + "s%s\n" ) % ( optName, desc )
                    out += outShort

            # }
        # }
        return out
    # }
# }


# DirUtl #########################
class DirUtl:
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

    @staticmethod
    def empty():
        return "";

    def __init__( self ):
        pass

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
        ( out, err ) = proc.communicate()  # @UnusedVariable
        return out
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
        if StrUtl.get().isNumberString( value ):
            return False
        if StrUtl.get().isString( value ) and ( value == "true" or value == "false" ) :
            return False
        return True


# MavenDescriptor #########################
class MavenDescriptor:
    __groupId = None;
    __artifact = None;
    __version = None;
    __packaging = None;

    def __init__( self, groupId, artifactId, version, packaging='jar' ):  # {
        self.__groupId = groupId;
        self.__artifact = artifactId;
        self.__version = version;
        self.__packaging = packaging;
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

