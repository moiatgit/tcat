#! /usr/bin/env python
# encoding: utf-8
#
# Given a text, this program scores it for all the layouts present
# at cwd directory
#
import sys
import urllib
import os, codecs, re
import operator
#
from glob import glob
#
from BeautifulSoup import BeautifulSoup
from KeyDistance import KeyDistance
from Layout import KeyboardLayout
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
            index_x = layout.symbols.index(x)
            index_y = layout.symbols.index(y)
            parells.append((index_x, index_y))
    return parells

def score_layout(layout, kd, text):
    parells = genera_parells(text, layout)
    score = 0
    for p in parells:
        score += kd.distances.get(p, 0)
    return score
#
def analyze_text(layouts, kd, source, text):
    """ creates a report for text considering scores for each layout """
    results = dict()
    for l in layouts:
        score = score_layout(layouts[l], kd, text)
        results[l]=score

    sorted_results = sorted(results.iteritems(), key=operator.itemgetter(1))
    for l, score in sorted_results:
        print "%s (%s) [%s]: %s"%(source, len(text), l, score)
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
                html = urllib.urlopen(f)
                soup = BeautifulSoup(html)
                raw = soup.body.getText()
            except:
                print "ERROR processing %s url"%f
        if raw:
            text = ""
            for ch in raw:
                lletres = normalitza_lletra(ch)
                text += "".join(lletres)  # awfull performance I know
            analyze_text(layouts, kd, f, text)
#
if __name__=="__main__":
    sys.exit(main())

