#! /usr/bin/env python
# encoding: utf-8
#
# This class implements a comfort keys layout
# It consists on a comfort index for each key in a keyboard
#
# Keys considered are (in a qwerty layout):
#   º1234567890'¡
#    qwertyuiop`+
#    asdfghjklñ´ç
#   <zxcvbnm,.-

# On these premises, keys are numbered from left to right and from top to
# bottom as follow:
#   00 01 02 03 04 05 06 07 08 09 10 11 12
#      13 14 15 16 17 18 19 20 21 22 23 24
#      25 26 27 28 29 30 31 32 33 34 35 36
#   37 38 39 40 41 42 43 44 45 46 47

# Comfort key index can be defined in a text file containing at least 48
# positive integer values (white spaces and extra integers ignored) and will be
# considered in the corresponding order previously defined.
#
# Default values are all keys set to index 1
#
# Note: this code does not pursues robustness in this first attempt
# Therefore, it will break if, for instance, you pass it a non-existent file
#
import sys, os.path
#
class ConfortKeys:
    def __init__(self, filename=None):
        if filename:
            self.loadConfortKeys(filename)
        else:
            self.setDefaultConfortKeys()

    def loadConfortKeys(self, filename):
        values = open(filename).read().split()
        self.keys = dict(enumerate([int(x) for x in values[:48]]))

    def setDefaultConfortKeys(self):
        self.keys = dict([(x, 0) for x in range(48)])

    def confortIndex(self, key):
        """ returns the confort index for key """
        return self.keys[key]

    def lowestIndex(self):
        """ returns the lowest confort index """
        return min(self.keys.values())

    def highestIndex(self):
        """ returns the highest confort index """
        return max(self.keys.values())

    def keysOfIndex(self, index):
        """ returns the keys that share the index """
        return [ k for k in self.keys if self.keys[k]==index]
#
def main():
    """ performs a simple test """
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = raw_input("Filename of the confort key indexes: ")
    if os.path.isfile(filename):
        ck = ConfortKeys(filename)
        print "Loaded %s"%filename
    else:
        ck = ConfortKeys()
        print "Loaded defaults"

    li = ck.lowestIndex()
    hi = ck.highestIndex()
    print "Lowest index: %s"%li
    for i in range(li, hi):
        print "keys of index %s: %s"%(i, ck.keysOfIndex(i))
    return 0
#
if __name__=="__main__":
    sys.exit(main())

