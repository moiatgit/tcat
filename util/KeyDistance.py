#! /usr/bin/env python
# encoding: utf-8
#
# Encapsulates key distances from a file with triplets: 
#   key1_id key2_id distance
# It considers reverse order pair with same distance
# Those pair of keys not appearing in the file are supposed 0 distant
#
import sys, os
#
class KeyDistance:
    def __init__(self, filename=None):
        if filename:
            self.loadDistance(filename)
        else:
            self.distances = dict()

    def loadDistance(self, filename):
        self.distances = dict() # (k1, k2): distance
        values = open(filename).read().split()
        triplets = zip(*[iter(values)]*3)
        for t in triplets:
            self.distances[(int(t[0]), int(t[1]))]=float(t[2])
            self.distances[(int(t[1]), int(t[0]))]=float(t[2])
#
def main():
    """ performs a simple test """
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = raw_input("Filename of the comfort key indexes: ")
    if os.path.isfile(filename):
        kd = KeyDistance(filename)
        print "Loaded %s"%filename
    else:
        kd = KeyDistance()
        print "Loaded defaults"

    for k in kd.distances:
        print k, kd.distances[k]
#
if __name__=="__main__":
    sys.exit(main())

