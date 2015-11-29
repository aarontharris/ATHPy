#!/usr/bin/python

from ATHPy import *  # @UnusedWildImport

def main():  # {
    opts = GetOpts()
    opts.addDescription( "Install ATHPy.py to the python path so that its widely available" )
    opts.addDescription( "By default ATHPy.py is installed to the python site-packages or dist-packages folder" )
    opts.addDescription( "You may override the path with --path=/path/to/install" )
    opts.add( "path", "p", "string", False, "Override the default path" )

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

if __name__ == '__main__': main()
