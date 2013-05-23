#! /usr/bin/env python
# encoding: utf-8
# computes sys.argv[1:] layouts scores
#
import sys
import codecs
from SymbolFreq import SymbolFreq
from confortkeys import ConfortKeys
from Layout import KeyboardLayout
#

#
def main():
    freq = SymbolFreq('frequencies.dat')
    ckeys = ConfortKeys('confortkeyprefs.dat')
    for l in sys.argv[1:]:
        if l.startswith("layout."):
            symbols = codecs.open(l, "r", "utf-8").read()
            layout = KeyboardLayout(symbols)
            score = ckeys.scoreLayout(layout, freq)
            print "[%s]: %s"%(l, score)
#
if __name__=="__main__":
    sys.exit(main())

