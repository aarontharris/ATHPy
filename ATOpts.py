
import enum
from ATHPy3 import StrUtl


class Typ(enum.Enum):
    STRING = 1
    BOOL = 2
    CSV = 3
    INT = 4
    FLOAT = 5
    DATE = 6
    FILE = 7
    FILE_EXIST = 8
    FOLDER = 9
    FOLDER_EXIST = 10

class Opt: # {
    __lng:str = ""
    __shrt:str = ""
    __typ:Typ = Typ.STRING
    __req:bool = False
    __desc:str = ""
    __defaultVal = None
    __visible:bool = True
    __positional:bool = False

    def __init__( self, lng, shrt, typ:Typ, req, desc, defaultVal=None, visible=True ): # {
        self.__lng=lng
        self.__shrt=shrt
        self.__typ=typ
        self.__req=req
        self.__desc=desc
        self.__defaultVal=defaultVal
        self.__visible=visible
    # }

    def pos( self ): # {
        self.__positional = True
        return self
    # }

    def describe(self): # {
        print("Opt(long='%s',short='%s',type='%s',req='%s',desc='%s',default='%s',visible='%s',positional='%s')" % 
        (self.__lng, self.__shrt, self.__typ, self.__req, self.__desc, self.__defaultVal, self.__visible, self.__positional))
    # }

    def getLong(self): return self.__lng
    def getShort(self): return self.__shrt
    def getType(self): return self.__typ
    def isReq(self): return self.__req
    def getDesc(self): return self.__desc
    def getDef(self): return self.__defaultVal
    def isVisible(self): return self.__visible
    def isPos(self): return self.__positional
# }

class ATOpts: # {
    __ = {}
    __opts = []
    __desc:str = ""
    __debug:bool = False

    def __init__(self, debug=False): # {
        self.__debug = debug
        pass
    # 

    def addDescription( self, description ): # {
        self.__desc = description
    # 

    # Overrides if key is already present
    # key is based on 'long'
    # @throws( Exception ) # when 'long' nor 'short' are present
    # @throws( Exception ) # when a positional Opt is added after a non positional Opt
    def add( self, opt:Opt ): # {
        self.__opts.append(opt)
        opts = self.__opts
        if ( len(opts) > 0 and opts[-1].isPos() ):
            raise Exception("err")
    # }

    # @param - key - the key associated with the value
    # @param - defaultVal - used only when key is present
    # @return - None if not found. return Typ matches added Typ
    def get( self, key, defaultVal=None ): # {
        pass
    # }

    def build( self, sysArgs ): # {
        for arg in sysArgs[1:]: # {
            pass

            # any leading args without '--'
                # match by order and type

            

            # all remaining args must lead with '--' or err
                # match by name

            # 

            
        # }
    # }

    def buildSafe( self, sysArgs ): # {
        pass
    # }

    def usage( self ): # {
        pass
    # }

    def describe(self): # {
        for opt in self.__opts:
            opt.describe()
    # }
# }