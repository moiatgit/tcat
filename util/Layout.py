#! /usr/bin/env python
# encoding: utf-8
#
# Implements a keyboard layout
# A layout is composed of 35 keys
# Each key has a symbol representing it.
# At this point, just level 1 symbols (the ones that appear by pressing
# directly the key) are considered
#
import sys
import codecs
#
_NUM_OF_KEYS = 35
#
class KeyboardLayout:
    def __init__(self, symbols):
        self.symbols = ' ' + symbols[:_NUM_OF_KEYS]

    def strsymbols(self):
        return '  ' + '  '.join(self.symbols[:12])   + '\n' +    \
               '  ' + '  '.join(self.symbols[12:24]) + '\n' +    \
               '  '.join(self.symbols[24:])          + '\n'

    @staticmethod
    def from_file(filename):
        """ returns a KeyboardLayout from the filename
            Ignores any char bellow 32 in file. """
        raw = codecs.open(filename, "r", "utf-8").read()
        symbols = "".join([ ch for ch in raw if ord(ch) > 32 ])
        return KeyboardLayout(symbols)
#
