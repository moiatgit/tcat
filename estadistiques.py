#! /usr/bin/env python
# encoding: utf-8
#
import sys, re
import codecs
import nltk
#
def genera_from_raw(raw, fd):
    """ genera els estats de raw al fitxer """
    fdist = nltk.FreqDist(ch.lower() for ch in raw if ch not in " \n")
    for k in fdist:
        fd.write("%s,%s\n"%(k,fdist[k]))

def genera_parells_from_raw(raw, fd):
    """ genera els estats de raw (freqüència de parelles de lletres)
    al fitxer fd """
    parells = [ vs for vs in re.findall(r'[a-z]{2}', raw.lower()) ]
    f = nltk.FreqDist(parells)
    for k in f:
        fd.write("%s,%s\n"%(k,f[k]))

def genera_estats(fitxer_origen, fitxer_destinacio, codificacio=""):
    if codificacio == "":
        raw = open(fitxer_origen).read()
        fout = open(fitxer_destinacio, "w")
    else:
        raw = codecs.open(fitxer_origen, encoding=codificacio).read()
        fout = codecs.open(fitxer_destinacio, "w", codificacio)

    genera_from_raw(raw, fout)
    fout.close()
#
def genera_parells(fitxer_origen, fitxer_destinacio, codificacio=""):
    if codificacio == "":
        raw = open(fitxer_origen).read()
        fout = open(fitxer_destinacio, "w")
    else:
        raw = codecs.open(fitxer_origen, encoding=codificacio).read()
        fout = codecs.open(fitxer_destinacio, "w", codificacio)
    genera_parells_from_raw(raw, fout)
    fout.close()

#
def obte_continguts(nom_fitxer, codificacio=""):
    if codificacio == "":
        raw = open(nom_fitxer).read()
    else:
        raw = codecs.open(nom_fitxer, encoding=codificacio).read()
    return raw

def obte_destinacio(nom_fitxer, codificacio=""):
    if codificacio == "":
        fout = open(nom_fitxer, "w")
    else:
        fout = codecs.open(nom_fitxer, "w", codificacio)
    return fout
#
def main():
    raw = obte_continguts(sys.argv[1], "utf-8")
    fd  = obte_destinacio(sys.argv[2], "utf-8")
    genera_from_raw(raw, fd)
    genera_parells_from_raw(raw, fd)
    fd.close()
    return 0
#
if __name__=="__main__":
    sys.exit(main())

