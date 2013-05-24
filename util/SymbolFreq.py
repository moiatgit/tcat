#! /usr/bin/env python
# encoding: utf-8
# 
# Encapsulates a simple map of symbols with its pre-computed
# frequencies obtained from a file
#
import sys
import codecs
#
_NUM_OF_KEYS = 35
#
class SymbolFreq:
    def __init__(self, filename=None):
        if filename:
            self.loadFreq(filename)
        else:
            self.setDefaultFreq()

    def loadFreq(self, filename):
        values = codecs.open(filename, "r", "utf-8").read().split()
        freq = dict()
        for i in range(0, _NUM_OF_KEYS*2, 2):
            freq[values[i]]=float(values[i+1])
        self.normalize_freqs(freq)

    def normalize_freqs(self, freq):
        """ given a frequency dict, it normalizes it in a %
        having the highest frequency a 100% and the lowest a 0% """
        l = min(freq.values())
        h = max(freq.values()) - l
        self.freq = dict()
        for k in freq.keys():
            self.freq[k] = (freq[k]-l)/h

    def setDefaultFreq(self):
        self.freq = dict([(x, 1.0/_NUM_OF_KEYS) for x in range(_NUM_OF_KEYS)])

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

