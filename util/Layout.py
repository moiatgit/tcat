#! /usr/bin/env python
# encoding: utf-8
#
# Implements a keyboard layout obtained from a file.
  A layout is composed of 48 keys
  Each key has ... KEEP WITH THIS!
#
import sys
#
class KeyboardLayout:
    def __init__(self, filename=None):
        if filename:
            self.loadLayout(self, filename)
        else:
            self.setDefaultLayout()
#
def main():
    pass
#
if __name__=="__main__":
    sys.exit(main())

