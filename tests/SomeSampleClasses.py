
class Polygon:
    __sides = 0
    __color = None
    __dithered = False
    __filled = False

    def __init__( self, sides ):
        self.__sides = sides

    def getSides( self ):
        return self.__sides

    def setColor( self, color, dithered=False, filled=False, **opts ):
        self.__color = color
        self.__dithered = dithered
        self.__filled = filled
        # params=reversed
        if opts.get( "params" ) == "reversed":
            print( "Reverse" )
            self.__filled = dithered  # absolutely terrible
            self.__dithered = filled  # absolutely terrible

    def describe( self ):
        return "sides=%r, color=%r, dithered=%r, filled=%r" % ( self.__sides, self.__color, self.__dithered, self.__filled )

    def __nonzero__( self ):
        """Used for conditionals on this object"""
        return True

    def __len__( self ):
        """When the len(polygon) is used, this is called.  Also called for conditionals when __nonzero__ is not defined."""
        return 1

class Triangle( Polygon ):
    def __init__( self ):
        Polygon.__init__( self, 3 )

class Square( Polygon ):
    def __init__( self ):
        Polygon.__init__( self, 4 )

class Pentagon( Polygon ):
    def __init__( self ):
        Polygon.__init__( self, 5 )

class Hexagon( Polygon ):
    def __init__( self ):
        Polygon.__init__( self, 6 )

class Heptagon( Polygon ):
    def __init__( self ):
        Polygon.__init__( self, 7 )

class Octogon( Polygon ):
    def __init__( self ):
        Polygon.__init__( self, 8 )
