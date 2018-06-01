#!/usr/bin/env python2.7

# For more info see: https://regexone.com/references/python

import imports_standardized as imps

import re # Regular Expression

from ATHPy import Regx

def basicRegex(): # {
    regex = "[A-Za-z]+"
    input = "Hello World"
    if ( re.search( regex, input ) ):
        print "Found it"
# }

def matchRegex(): # {
    regex = "[A-Za-z]+"
    input = "Hello World"

    match = re.search( regex, input )
    print ( "First match start=%s, end=%s" % (match.start(), match.end()) )
# }

def groupRegex(): # {
    regex = "[A-Za-z]+"
    input = "Hello World"

    match = re.search( regex, input ) # search finds only the first, its not a global search
    print( "Group0='%s'" % (match.group(0)) )
    # print( "Group1='%s'" % (match.group(1)) ) # ERR, there is no group 1
# }

def findallRegex(): # {
    regex = "[A-Za-z]+"
    input = "Hello World"

    # global search returns a collection
    # BE CAREFUL this will load the entire contents into memory and all matches into memory
    # for you to process. If the input is large or many matches expected, finditr may be better
    matches = re.findall( regex, input ) 
    for match in matches: # match is a string
        print ( "found %s" % (match) )
# }

def finditerRegex(): # {
    regex = "[A-Za-z]+"
    input = "Hello World"

    # global search returns a collection
    # BE CAREFUL this will load the entire contents into memory and all matches into memory
    # for you to process. If the input is large or many matches expected, finditr may be better
    matches = re.finditer( regex, input ) 
    for match in matches: # match is a match obj
        # input[#1:#2] // this is the synta
        print ( "found match %s @ start=%s, end=%s" % (input[match.start():match.end()], match.start(), match.end()) )
# }

def finditerRegexAdvanced(): # {
    regex = r"(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})"
    #regex = r"(\d{2}|\d{4})"
    input = "7/5/79, 8/16/82, 2/29/16"

    # global search returns a collection
    # BE CAREFUL this will load the entire contents into memory and all matches into memory
    # for you to process. If the input is large or many matches expected, finditr may be better
    matches = re.finditer( regex, input ) 
    for match in matches: # match is a match obj
        # input[#1:#2] // this is the synta
        #print ( "found match %s @ start=%s, end=%s" % (input[match.start():match.end()], match.start(), match.end()) )
        print( "whole group match='%s', mo='%s', day='%s', yr='%s'" % (
            match.group(0),
            match.group(1),
            match.group(2),
            match.group(3)
            ) )
# }

def searchAndReplaceRegexMultiline(): # {
    regex = r"Bob"
    replace = "Aaron"
    input = "Hello my name is Bob\nDid I mention my name is Bob"
    result = re.sub(regex, replace, input, 0, re.MULTILINE)
    print result
# }

def searchAndReplaceRegexMultilineAdvanced(): # {
    input = "Hello my name is Bob"
    input += "\n"
    input += "Did I mention my name is Bob"
    input += "\n"
    input += "Even though I am Bob, he is also Bob"
    input += "\n"
    input += "We are Bob"

    output = ''
    lastPos = 0
    regex = re.compile(r"(Bob)", re.MULTILINE)
    matches = regex.finditer(input)
    for match in matches:
        if match:
            repl = "Aaron"
            output += input[lastPos:match.start()]
            output += repl
            lastPos = match.start() + len(match.group(1))
    print "--"
    print output
# }

def searchAndReplaceSimplified(): # {
    input = "Hello my name is Bob"
    input += "\n"
    input += "Did I mention my name is Bob"
    input += "\n"
    input += "Even though I am Bob, he is also Bob"
    input += "\n"
    input += "We are Bob"

    inc = 0
    Regx.replace( r"Bob", input, searchAndReplaceSimplifiedSearchResultDelegate )
# }

def searchAndReplaceSimplifiedSearchResultDelegate(): # {
    return
# }

def __main(): # {
    basicRegex()
    matchRegex()
    groupRegex()
    findallRegex()
    finditerRegex()
    finditerRegexAdvanced()
    searchAndReplaceRegexMultiline()
    searchAndReplaceRegexMultilineAdvanced()
# }

if __name__ == '__main__': __main()