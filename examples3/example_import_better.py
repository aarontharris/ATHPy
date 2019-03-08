#!/usr/bin/env python3

# don't need these anymore as the "imports_standardized" does it for us
# import os,sys
# sys.path.append( os.path.abspath("./ATHPy/") )

# import our importer script 
import imports_standardized as imports
#sys.path.append( os.environ.get( "ATHPYDIR", "../ATHPy/" ) )

# Even though our importer script handled the lib path
# we still need to namespace our static imports
# without this, we could probably use ATHPy.EnvUtl directly?
from ATHPy3 import EnvUtl

print(EnvUtl.execute("ls"))

# We can also reference methods defined in the importer script
imports.someReusableMethod()
