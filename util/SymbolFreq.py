#! /usr/bin/env python
# encoding: utf-8
# 
# Encapsulates a simple map of symbols with its pre-computed
# frequencies obtained from a file
#
import sys
#
class SymbolFreq:
    def __init__(self, filename=None):
        self.numberofkeys = 35
        if filename:
            self.loadFreq(filename)
        else:
            self.setDefaultFreq()

    def loadFreq(self, filename):
        values = open(filename).read().split()
        self.freq = dict()
        for i in range(0, self.numberofkeys, 2):
            self.freq[values[i]]=values[i+1]

    def setDefaultFreq(self):
        self.freq = dict([(x, 1.0/self.numberofkeys) for x in range(self.numberofkeys)])

#
def main():
    if len(sys.argv) > 1:
        sf =  SymbolFreq(sys.argv[1])
    else:
        sf = SymbolFreq()

    print sf.freq
#
if __name__=="__main__":
    sys.exit(main())

