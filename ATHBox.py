
class Box: # {
    __h = 0
    __w = 0
    def __init__( self, h, w ): # {
        self.__h = h
        self.__w = w
    # }

    def describe( self ): # {
        print ( "%s x %s" % (self.__h, self.__w) )
    # }
# }
