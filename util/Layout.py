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
#
_NUM_OF_KEYS = 35
#
class KeyboardLayout:
    def __init__(self, symbols):
        self.symbols = symbols[:_NUM_OF_KEYS]

    def strsymbols(self):
        return '  ' + '  '.join(self.symbols[:12])   + '\n' +    \
               '  ' + '  '.join(self.symbols[12:24]) + '\n' +    \
               '  '.join(self.symbols[24:])          + '\n'

#
