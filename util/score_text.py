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
from tempfile import NamedTemporaryFile
#
_FILENAME="/tmp/fitxer_normalitzat.txt"
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
def analyze_text(layouts, kd, source):
    """ creates a report for text considering scores for each layout """
    # result initialization
    results = dict()
    for l in layouts:
        results[l]=0    # layout: distance

    # process text
    fd = codecs.open(_FILENAME, "r", "utf-8")
    parells = list()
    prev = ' '
    while True:
        ch = fd.read(1)
        if not ch:
          break
        if ch <> prev and ch <> ' ':
            for l in layouts:
                symbols = layouts[l].symbols
                index_x = symbols.index(prev) if prev in symbols else 0
                index_y = symbols.index(ch) if ch in symbols else 0
                p = (index_x, index_y)
                results[l] += kd.distances.get(p, 0)
        prev = ch
    fd.close()

    min_distance = min(results.values())
    sorted_results = sorted(results.iteritems(), key=operator.itemgetter(1))
    print "\nSource: %s"%source
    for l, score in sorted_results:
        print "\t%-9s:\t%s (%0.2f%%)"%(l, score, (score-min_distance)/min_distance)
#
def load_layouts():
    """ load all the layouts available at cwd and returns them
    in a dict() layout_name:Layout """
    layouts = dict()
    for f in glob("layout.*.dat"):
        l = KeyboardLayout.from_file(f)
        m = re.match("layout\.(.*)\.dat", f)
        name = m.group(1)
        layouts[name]=l
    return layouts
#
def main():
    # kd = KeyDistance('keydistance.dat')
    kd = KeyDistance('pairconfort.dat')
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
            print "Loaded raw"
            tf = codecs.open(_FILENAME, "w", "utf-8")
            for ch in raw:
                tf.write("".join(normalitza_lletra(ch)))
            tf.close()
            raw = None
            print "Encoded raw"
            analyze_text(layouts, kd, f)
#
if __name__=="__main__":
    sys.exit(main())

