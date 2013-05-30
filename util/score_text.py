#! /usr/bin/env python
# encoding: utf-8
#
# Given a text, this program scores it for all the layouts present
# at cwd directory
#
import sys
import urllib2
import os, codecs, re
import operator
#
from glob import glob
#
from BeautifulSoup import BeautifulSoup
from KeyDistance import KeyDistance
from Layout import KeyboardLayout
from HandDistrib import HandDistribution
#
def normalitza_lletra(lletra):
    """ retorna la lletra normalitzada. És a dir, elimina els
    accents, dièresis etc. i converteix tots els caràcters no suportats
    a espai.
    Per les lletres que requereixen composició (ex. à) retorna el parell
    ['a', '`']"""
    lletra = lletra.lower()
    if not re.match(u'[-+.,<a-zñçàáèéíïòóúû`´]', lletra):
        lletra= [u' ']
    elif lletra == u"à":
        lletra = [u'`', 'a']
    elif lletra == u"á":
        lletra = [u'´', 'a']
    elif lletra == u"è":
        lletra = [u'`', 'e']
    elif lletra ==  u"é":
        lletra = [u'´', 'e']
    elif lletra == u'í':
        lletra = [u'´', 'i']
    elif lletra == u'ï':
        lletra = [ u'´', 'i']
    elif lletra == u'ò':
        lletra = [u'`', 'o']
    elif lletra == u'ó':
        lletra = [u'´', 'o']
    elif lletra == u'ú':
        lletra = [u'´', 'u']
    elif lletra == u'ü':
        lletra = [u'´', 'u']
    elif lletra == u':':
        lletra = ['.']
    elif lletra == u';':
        lletra = [',']
    elif lletra == u'*':
        lletra = ['+']
    elif lletra == u'_':
        lletra = ['-']
    elif lletra == u'>':
        lletra = ['<']
    return lletra
#
def genera_parells(text, layout):
    """ genera els parells de lletres de raw i retorna les posicions
        corresponents al layout """
    parells = list()
    for i in range(len(text)-1):
        x, y = text[i], text[i+1]
        if x <> y and i <> ' ':
            symbols = layout.symbols
            index_x = symbols.index(x) if x in symbols else 0
            index_y = symbols.index(y) if y in symbols else 0
            parells.append((index_x, index_y))
    return parells

def score_hand_distrib(hd, k1, k2):
    """ computes and returns whether the two keys belong to the same
    hand """
    if (min(k1, k2)>0): # 0 key (e.g. space bar) is not considered
        res = int(not(bool(hd.distrib[k1]) <> bool(hd.distrib[k2])))
    else:
        res = 0
    return res
#
def score_layout(layout, kd, hd, text):
    parells = genera_parells(text, layout)
    score_distance = score_hands = 0
    for p in parells:
        score_distance += kd.distances.get(p, 0)
        score_hands += score_hand_distrib(hd, *p)
    return score_distance, score_hands
#
def analyze_text(layouts, kd, hd, source, text):
    """ creates a report for text considering scores for each layout """
    min_distance = min_hand = sys.maxint
    results = dict()
    for l in layouts:
        score = score_layout(layouts[l], kd, hd, text)
        min_distance = min(min_distance, score[0])
        min_hand = min(min_hand, score[1])
        results[l]=score

    sorted_results = sorted(results.iteritems(), key=operator.itemgetter(1))
    print "\nSource (%s sym): %s"%(len(text), source)
    for l, score in sorted_results:
        score_distance, score_hands = score
        pcent_distance = 100*(score_distance - min_distance) / min_distance
        pcent_hand = 100*(score_hands - min_hand) / min_hand
        print "\t[%s]:\tdistance=%10s (%0.2f%%)\thands=%s (%4.2f%%)"%(l, score_distance, pcent_distance, score_hands, pcent_hand)
#
def load_layouts():
    """ load all the layouts available at cwd and returns them
    in a dict() layout_name:Layout """
    layouts = dict()
    for f in glob("layout.*.dat"):
        symbols = codecs.open(f, 'r', 'utf-8').read()
        l = KeyboardLayout(symbols)
        m = re.match("layout\.(.*)\.dat", f)
        name = m.group(1)
        layouts[name]=l
    return layouts
#
def main():
    kd = KeyDistance('keydistance.dat')
    hd = HandDistribution('hand_distribution.dat')
    layouts = load_layouts()
    for f in sys.argv[1:]:
        raw = None
        if os.path.isfile(f):
            try:
                raw = codecs.open(f, "r", "utf-8").read()
            except:
                print "ERROR processing %s file"%f
        else:
            try:
                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                infile = opener.open(f)
                html = infile.read()
                soup = BeautifulSoup(html)
                raw = soup.body.getText()
            except:
                print "ERROR processing %s url"%f
        if raw:
            lletres = []
            for ch in raw:
                lletres += normalitza_lletra(ch)
            raw = None
            text = "".join(lletres)
            analyze_text(layouts, kd, hd, f, text)
#
if __name__=="__main__":
    sys.exit(main())

