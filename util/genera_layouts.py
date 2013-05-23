#! /usr/bin/env python
# encoding: utf-8
#
#   Generates a number of layouts with better scores
import sys, time
from itertools import permutations
from Layout import KeyboardLayout
from SymbolFreq import SymbolFreq
from confortkeys import ConfortKeys
#
_NUM_OF_KEYS = 35
_MAX_LAYOUTS = 1000000   # max number of layouts to keep
_MAX_SAME_SCORED_LAYOUTS = 10000   # max number of layouts with same score to keep
#
def save_layouts(keyboards):
    """ saves uptonow keyboards """
    f = open("scoredlayouts.dat", "w")
    for score in keyboards.keys():
        f.write("\n%s\n"%("-"*80))
        f.write("\nscore: %s\n"%score)
        f.write("\n%s\n"%("="*80))
        for kb in keyboards[score]:
            f.write(kb.strsymbols())
            f.write("\n%s\n"%("-"*80))
    f.close()

def main():
    keyboards = dict()  # score: [layout]
    npermuts = 0
    minscore = 10000000
    maxscore = 10000000
    numlayouts = 0
    symbols = open('keysymbols.dat', 'r').read().split()[:_NUM_OF_KEYS]
    freq = SymbolFreq('frequencies.dat')
    ckeys = ConfortKeys('confortkeyprefs.dat')
    for p in permutations(symbols, _NUM_OF_KEYS):
        npermuts += 1
        layout = KeyboardLayout(p)
        score = ckeys.scoreLayout(layout, freq)
        if score < maxscore:
            if score in keyboards.keys():
                if len(keyboards[score])<_MAX_SAME_SCORED_LAYOUTS:
                    keyboards[score].append(layout)
                    numlayouts += 1
            else:
                keyboards[score]=[layout]
                numlayouts += 1
            if numlayouts > _MAX_LAYOUTS:
                m = min(keyboards.keys())
                nremove = len(keyboards[m])
                numlayouts -= nremove
                del(keyboards[m])
                maxscore = m
                print "Removed score %s: %s layouts"%(m, nremove)
            if minscore > score:
                minscore = score
                print "Permutations %s"%npermuts
                print "Score: %s"%score
                print layout.strsymbols()
                print "-"*80
                save_layouts(keyboards)
    save_layouts(keyboards)
#
if __name__=="__main__":
    sys.exit(main())

