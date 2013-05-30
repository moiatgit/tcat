#! /usr/bin/env python
# encoding: utf-8
# 
# Encapsulates a map of pair of symbols with its pre-computed
# frequencies obtained from a file
#
import sys
import codecs
from collections import defaultdict
import operator
#
class PairFreq:
    def __init__(self, filename):
        self.loadFreq(filename)

    def loadFreq(self, filename):
        fd = codecs.open(filename, "r", "utf-8")
        self.freq = defaultdict(list)
        for lin in fd.readlines():
            p, vtext = lin.split()
            v = float(vtext)
            s1, s2 = p[0], p[1]
            self.freq[s1].append((s2, v))
            self.freq[s2].append((s1, v))

    def freq_of_symbol(self, symbol):
        """ returns the frequence list for symbol
        sorted by frequency """
        sorted_results = sorted(self.freq[symbol], key=operator.itemgetter(1), reverse=True)
        return sorted_results
#
def main():
    pf = PairFreq('pair_freq.dat')
    for s, f in pf.freq_of_symbol(sys.argv[1]):
        print s, f
#
if __name__=="__main__":
    sys.exit(main())

