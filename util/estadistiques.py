#! /usr/bin/env python
# encoding: utf-8
#
import sys, re
import codecs
import operator
#
from collections import defaultdict
#
def normalitza_lletra(lletra):
    """ retorna la lletra normalitzada. És a dir, elimina els
    accents, dièresis etc. i converteix tots els caràcters no suportats
    a espai.
    Per les lletres que requereixen composició (ex. à) retorna el parell
    ['a', '`']"""
    lletra = lletra.lower()
    if not re.match(u'[-+.,<a-zñçàáèéíïòóúû]', lletra):
        lletra= [u' ']
    elif lletra == u"à":
        lletra = [u'`', u'a']
    elif lletra == u"á":
        lletra = [u'´', u'a']
    elif lletra == u"è":
        lletra = [u'`', u'e']
    elif lletra ==  u"é":
        lletra = [u'´', u'e']
    elif lletra == u'í':
        lletra = [u'´', u'i']
    elif lletra == u'ï':
        lletra = [ u'´', u'i']
    elif lletra == u'ò':
        lletra = [u'`', u'o']
    elif lletra == u'ó':
        lletra = [u'´', u'o']
    elif lletra == u'ú':
        lletra = [u'´', u'u']
    elif lletra == u'ü':
        lletra = [u'´', u'u']
    elif lletra == u':':
        lletra = [u'.']
    elif lletra == u';':
        lletra = [u',']
    elif lletra == u'*':
        lletra = [u'+']
    elif lletra == u'_':
        lletra = [u'-']
    elif lletra == u'>':
        lletra = [u'<']
    return lletra
#
def genera_parells(text):
    """ genera els parells de lletres.
        Elimina parells de la mateixa lletra.
        Només genera una combinació de cada parell (és a dir
        les aparicions 'ea' es converteixen a 'ab' """
    parells = list()
    for i in range(len(text)-1):
        x, y = text[i], text[i+1]
        if u' ' not in [x, y] and x<>y:
            par = "%s%s"%(x,y) if x < y else "%s%s"%(y,x)
            parells.append(par)
    return parells
#
def genera_estats(fin, fout):
    """ genera els estats de cada lletra i de cada parell i 
    els deixa al fitxer fd """
    dist_lletres = defaultdict(int)
    dist_parells = defaultdict(int)
    ant = list()     # lletres anteriors
    while True:
        try:
            ch = fin.read(1)
        except:
            print "WARNING: problem reading a char"
            continue
        if not ch:
            break
        ant += normalitza_lletra(ch)
        while (len(ant)>1):
            lletra = ant.pop(0)
            if lletra == ' ':
                continue
            dist_lletres[lletra] += 1
            if ant[0] == ' ' or ant[0] == lletra:
                ant.pop(0)
            else:
                par = "%s%s"%( (lletra, ant[0]) if lletra < ant[0] else (ant[0], lletra) )
                dist_parells[par] += 1

    guarda_estats(dist_lletres, fout)
    guarda_estats(dist_parells, fout)
#
def guarda_estats(fdist, fd):
    """ guarda els estats al fitxer ordenats per freqüència """
    for k,v in sorted(fdist.iteritems(), key=operator.itemgetter(1), reverse=True):
        fd.write("%s\t%s\n"%(k,v))
#
def main():
    fin = codecs.open(sys.argv[1], "r", encoding="utf-8")
    fout = codecs.open(sys.argv[2], "w", encoding="utf-8")
    # fin = open(sys.argv[1], "r")
    # fout = open(sys.argv[2], "w")
    genera_estats(fin, fout)
    fout.close()
    fin.close()
    return 0
#
if __name__=="__main__":
    sys.exit(main())

