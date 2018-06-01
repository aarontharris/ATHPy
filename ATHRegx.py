import re

# Regx ######################### # EX: See example_regex.py
class Regx: # {
    __matchNumber = 0
    __input = ''

    def __init__( self, input ): # {
        self.__matchNumber = 0
        self.__input = input
    # }

    def getMatchNum(self): return self.__matchNumber

    # Simple replace the sequences that match the given pattern
    # with the given replace value.
    # MULTILINE is ON
    def replace( self, pattern, replace ): # {
        input = self.__input
        output = ''
        lastPos = 0
        regex = re.compile(pattern, re.MULTILINE)
        matches = regex.finditer(input)
        for m in matches:
            if m:
                output += input[lastPos:m.start()]
                output += replace
                lastPos = m.start() + len(m.group(0))
        return output
    # }

    # Each instance in the input that matches the given pattern
    # will be given to the delegate, the value returned from the delegate
    # will be substituted in place of the original match
    def replaceDelegate( self, pattern, delegate ): # {
        input = self.__input
        output = ''
        lastPos = 0
        regex = re.compile(pattern, re.MULTILINE)
        matches = regex.finditer(input)
        match = Match()
        idx = 0
        for m in matches:
            if m:
                match.recycle(idx, m)
                repl = delegate(match)
                output += input[lastPos:m.start()]
                output += repl
                lastPos = m.start() + len(m.group(0))
                idx += 1
        return output
    # }
# } Regx

class Match: # {
    idx = 0
    match = None

    def recycle( self, idx, match ): # {
        self.idx = idx
        self.match = match
    # }
# }