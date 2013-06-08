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
import normalize_text
#
def analyze_text(layouts, kd, name, source):
    """ creates a report for text considering scores for each layout """
    # result initialization
    results = dict()
    for l in layouts:
        results[l]=0    # layout: distance

    # process text
    fd = codecs.open(source, "r", "utf-8")
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
    print "\nSource: %s"%name
    for l, score in sorted_results:
        print "\t%-9s:\t%s (%0.2f%%)"%(l, score, 100*(score-min_distance)/min_distance)
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
    kd = KeyDistance('pairconfort.dat')
    layouts = load_layouts()
    for f in sys.argv[1:]:
        dest = normalize_text.compose_dest_filename(f)
        if not os.path.exists(dest):
            normalize_text.save_normalized(dest, f)
        analyze_text(layouts, kd, f, dest)
#
if __name__=="__main__":
    sys.exit(main())

