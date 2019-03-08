#!/usr/bin/env python3

def __main():
  d = dict()
  key = 'key'
  d[key] = 'Yo'
  val=d.get('key', None)
  print ("Value='%s'\n" % (val))

if __name__ == '__main__': __main()