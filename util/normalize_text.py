#! /usr/bin/env python
# encoding: utf-8
#
# Given a text, this program normalizes it in order to be processed
# by other programs like score_text.py
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
_SOURCE_PATH="src/"
#
def normalitza_lletra(lletra):
    """ retorna la lletra normalitzada. És a dir, elimina els
    accents, dièresis etc. i converteix tots els caràcters no suportats
    a espai.
    Per les lletres que requereixen composició (ex. à) retorna el parell
    ['a', '`']"""
    lletra = lletra.lower()
    if lletra == u"à":
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
    elif lletra == ';':
        lletra = [',']
    elif lletra == '*':
        lletra = ['+']
    elif lletra == '_':
        lletra = ['-']
    elif lletra == '>':
        lletra = ['<']
    elif not re.match('[-+.,<a-z`´]', lletra):
        lletra = ' '
    return lletra
#
def normalitza_text(raw):
    """ generates a normalized text. It yields char by char """
    last = ' '
    for ch in raw:
        for lletra in normalitza_lletra(ch):
            if last <> lletra:
                last = lletra
                yield lletra
#
def compose_dest_filename(url):
    """ composes and returns the destination filename from the url """
    pref = ''
    if url.startswith('http://'):
        pref = os.path.dirname(url).lstrip('http://').replace('/','.')+'.'
    name = os.path.basename(url)
    dest = "%s%s%s.normalized"%(_SOURCE_PATH,pref,name)
    return dest
#
def get_raw(url):
    """ obtains raw contents from url.
        It loads everything on memory """
    raw = None
    if os.path.isfile(url):
        try:
            raw = codecs.open(url, "r", "utf-8").read()
        except:
            print "ERROR processing %s file"%url
    else:
        try:
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            infile = opener.open(url)
            html = infile.read()
            soup = BeautifulSoup(html)
            raw = soup.body.getText()
        except:
            print "ERROR processing %s url"%url
    return raw
#
def save_normalized(dest, source):
    """ saves normalized source text into destination file """
    tf = codecs.open(dest, "w", "utf-8")
    for lletra in normalitza_text(get_raw(source)):
        tf.write(lletra)
    tf.close()

def main():
    for f in sys.argv[1:]:
        dest = compose_dest_filename(f)
        if os.path.exists(dest):
            print "WARNING: file %s already exists. Remove it if re-normalization is required"%dest
            return
        save_normalized(dest, f)
#
if __name__=="__main__":
    sys.exit(main())

