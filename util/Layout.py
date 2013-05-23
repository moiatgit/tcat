#! /usr/bin/env python
# encoding: utf-8
#
# Implements a keyboard layout
# A layout is composed of 35 keys
# Each key has a symbol representing it.
# At this point, just level 1 symbols (the ones that appear by pressing
# directly the key) are considered
#
import sys
import itertools
import time
import SymbolFreq, confortkeys
#
_NUM_OF_KEYS = 35
#
class KeyboardLayout:
    def __init__(self, symbols):
        self.numberofkeys = _NUM_OF_KEYS
        if len(symbols)<> self.numberofkeys:
            raise
        self.symbols = symbols

    def strsymbols(self):
        return '\t' + '\t'.join(self.symbols[:12])   + '\n' +    \
               '\t' + '\t'.join(self.symbols[12:24]) + '\n' +    \
               '\t'.join(self.symbols[24:])          + '\n'

#
def main():
    symbols = open('keysymbols.dat', 'r').read().split()[:_NUM_OF_KEYS]
    for p in itertools.permutations(symbols, _NUM_OF_KEYS):
        layout = KeyboardLayout(p)
        freq = SymbolFreq.SymbolFreq('frequencies.dat')
        ckeys = confortkeys.ConfortKeys('confortkeyprefs.dat')

        print layout.strsymbols()
        print "-"*80
        time.sleep(1)
#
if __name__=="__main__":
    sys.exit(main())

