#!/usr/bin/python

from ATHPy import *  # @UnusedWildImport

# Global
opts = GetOpts()

def main():  # {
    opts.addDescription( "Install ATHPy.py to the python path so that its widely available" )
    opts.addDescription( "By default ATHPy.py is installed to the python site-packages or dist-packages folder" )
    opts.addDescription( "You may override the path with --path=/path/to/install" )

    opts.add( "path", "p", "string", False, "Override the default path" )
    opts.add( "help", "h", None, False, "Display Usage", method=handleHelp )

    if opts.buildSafe( sys.argv ):  # {
        path = opts.get( 'path', EnvUtl.getBestPythonLibDir() )
        help = opts.get( 'help', False )
        Log.d( "Help: '%s'" % help )
        try:
            DirUtl.copyFile( "./ATHPy.pyc", path )
            Log.d( "Installed to %s" % path )
        except IOError as err:
            Log.eMsg( err )  # likely a permission problem
        except Exception as err:
            Log.e( err )
    # }
# }

def handleHelp( val ):  # {
    # opts.usage()
    Log.d( "HandleHelp got %s" % val )
    return True
# }

if __name__ == '__main__': main()
