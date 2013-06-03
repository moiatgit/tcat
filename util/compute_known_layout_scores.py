#! /usr/bin/env python
# encoding: utf-8
# computes sys.argv[1:] layouts scores
#
import sys, re
from SymbolFreq import SymbolFreq
from comfortkeys import ConfortKeys
from Layout import KeyboardLayout
from KeyDistance import KeyDistance
from PairFreq import PairFreq
#
def compute_score_distance(kd, pf, layout):
    """ returns the score of the layout for the key distance
    having into account the pair frequencies """
    score = 0
    for symbol in pf.freq:
        k1 = layout.symbols.index(symbol)
        for s, pairfreq in pf.freq[symbol]:
            k2 = layout.symbols.index(s)
            distancia = kd.distances[(k1, k2)] if (k1, k2) in kd.distances else 0
            score += distancia * pairfreq
    return score
#
def main():
    freq = SymbolFreq('frequencies.dat')
    ckeys = ConfortKeys('comfortkeyprefs.dat')
    kd = KeyDistance('keydistance.dat')
    pf = PairFreq('pair_freq.dat')
    scores = list()
    for l in sys.argv[1:]:
        if l.startswith("layout."):
            layout = KeyboardLayout.from_file(l)
            score_confort = ckeys.scoreLayout(layout, freq)
            score_pairs = compute_score_distance(kd, pf, layout)
            m = re.match("layout\.(.*)\.dat", l)
            name = m.group(1)
            scores.append((score_pairs, score_confort, name))
    sorted_scores = sorted(scores)
    for score_pairs, score_confort, name in sorted_scores:
        print "[%s]: frq:%s \t confort:%s"%(name, score_pairs, score_confort)
#
if __name__=="__main__":
    sys.exit(main())

