#!/usr/bin/env python2.7

def __main(): # {
    test1()
# }

def test1(): # {
    a = "hello my name is %s and I'm %s years old" % ( 'Aaron', `39` )
    b = "hello my name is %s and I'm %s years old" % ( 'Carmen', `2` )
    log( a, b )

    log( "hello my name is %s and I'm %s years old" % ( 'Aaron', `39` ), "hello my name is %s and I'm %s years old" % ( 'Carmen', `2` ) )
# }

def log( a, b ): # {
    print a
    print b
# }

if __name__ == '__main__': __main()