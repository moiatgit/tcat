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

# Comfort key index can be defined in a text file containing just 48 positive
# integer values (white spaces ignored) and will be considered in the
# corresponding order previously defined.
#
# Default values are all keys set to index 1
#
import sys
#
class ConfortKeys:
    def __init__(self, filename=None):
        keys = dict()

#
def main():
    pass
#
if __name__=="__main__":
    sys.exit(main())

