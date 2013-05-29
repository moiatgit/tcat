#! /usr/bin/env python
# encoding: utf-8
#
# Encapsulates hand distributions from a file with pairs: 
#   key_id hand
# Where hand 0 for left and 1 for right

import sys, os
#
class HandDistribution:
    def __init__(self, filename):
        self.loadDistribution(filename)

    def loadDistribution(self, filename):
        self.distrib = dict() # k: hand
        values = open(filename).read().split()
        pairs = zip(*[iter(values)]*2)
        for p in pairs:
            self.distrib[int(p[0])]=int(p[1])
#
def main():
    """ performs a simple test """
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = raw_input("Filename of the hand distribution keys: ")
    if os.path.isfile(filename):
        hd = HandDistribution(filename)
        print "Loaded %s"%filename
        for k in hd.distrib:
            print k, hd.distrib[k]
    else:
        print "ERROR with file"

#
if __name__=="__main__":
    sys.exit(main())

