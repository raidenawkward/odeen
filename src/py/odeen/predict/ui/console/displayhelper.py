# coding = utf-8

import sys

class DisplayHelper:
    def displayLine(message, tag=None, newLine=True):
        string = ''

        if tag is not None:
            string = string + '[' + str(tag) + '] '

        string = string + str(message)

        if newLine:
            string = string + '\n'

        sys.stdout.write(string)
        sys.stdout.flush()