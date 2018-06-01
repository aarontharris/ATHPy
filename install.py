#!/usr/bin/python

from ATHPy import *  # @UnusedWildImport compiles ATHPy.py

# Global
opts = GetOpts()

def main():  # {
    opts.addDescription( "Install ATHPy.py to the python path so that its widely available" )
    opts.addDescription( "By default ATHPy.py is installed to the python site-packages or dist-packages folder" )
    opts.addDescription( "You may override the path with --path=/path/to/install" )
    opts.addDescription( "\n** Note: Make sure you have permission to the destination path, consider sudo ./install.py" )

    opts.add( "path", "p", "string", False, "Override the default path" )
    opts.add( "where", "w", None, False, "Display the actual default path", method=handleWhere )
    opts.add( "help", "h", None, False, "Display Usage", method=handleHelp )

    if opts.buildSafe( sys.argv ):  # {
        path = opts.get( 'path', EnvUtl.getBestPythonLibDir() )
        try:
            DirUtl.copyFile( "./ATHPy.pyc", path )
            Log.d( "Installed to %s" % path )
        except IOError as err:
            Log.eMsg( err )  # likely a permission problem
        except Exception as err:
            Log.e( err )
    # }
# }

def handleWhere( val ):  # {
    print EnvUtl.getBestPythonLibDir()
    exit()
# }

def handleHelp( val ):  # {
    print opts.usage()
    exit()
# }

if __name__ == '__main__': main()
