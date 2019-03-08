#!/usr/bin/env python3

import os, sys

# sys.path.append( os.environ.get( "ATHPYDIR" ) )
# from ATHPy3 import GetOpts

import getopt


def __main():  # {
    version = "1.0"
    verbose = False
    output_filename = "default.out"

    print("Hello World")

    try:
        options, remainder = getopt.getopt(
            sys.argv[1:], "o:v", ["output=", "verbose", "version="]
        )
    except getopt.GetoptError as err:
        print("ERROR:", err)
        sys.exit(1)

    print("OPTIONS   :", options)

    for opt, arg in options:
        if opt in ("-o", "--output"):
            output_filename = arg
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt == "--version":
            version = arg

    print("VERSION    :", version)
    print("VERBOSE    :", verbose)
    print("OUTPUT     :", output_filename)
    print("REMAINING  :", remainder)

# }

if __name__ == "__main__": __main()
