#! /usr/bin/env python
# encoding: utf-8
#
import sys, os
import codecs
import operator
#
from collections import defaultdict
#
import normalize_text
#
def genera_estats(fin, fout):
    """ genera els estats de cada lletra i de cada parell i 
    els deixa al fitxer fd """
    dist_lletres = defaultdict(int)
    dist_parells = defaultdict(int)
    dist_ternes  = defaultdict(int)
    ant = list()     # lletres anteriors
    while True:
        try:
            ch = fin.read(1)
        except:
            print "WARNING: problem reading a char"
            continue
        if not ch:
            break
        if ch == ' ':
            ant = list()    # buida la llista
        else:
            ant.append(ch)
            dist_lletres[ch] += 1
            l = len(ant)
            if (l > 1):
                par = (min(ant[-2:]), max(ant[-2:]))
                dist_parells[par] += 1
            if (l == 3):
                dist_ternes[tuple(ant)] += 1
                ant = list()
    guarda_estats(dist_lletres, fout)
    guarda_estats(dist_parells, fout)
    guarda_estats(dist_ternes, fout)
#
def guarda_estats(fdist, fd):
    """ guarda els estats al fitxer ordenats per freqüència """
    for k,v in sorted(fdist.iteritems(), key=operator.itemgetter(1), reverse=True):
        for i in k:
            print i.encode('utf-8'),'\t',
        print "\t%s"%v
#
def main():
    for f in sys.argv[1:]:
        dest = normalize_text.compose_dest_filename(f)
        if not os.path.exists(dest):
            normalize_text.save_normalized(dest, f)
        fin = codecs.open(dest, "r", encoding="utf-8")
        print "Stats of file: %s"%f
        genera_estats(fin, sys.stdout)
        fin.close()
    return 0
#
if __name__=="__main__":
    sys.exit(main())

