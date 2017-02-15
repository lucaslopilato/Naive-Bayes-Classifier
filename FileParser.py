# fileParser.py
# Class Responsible for handling all file IO
# Extracts useful information relative to Machine Problem 1
import sys
from collections import defaultdict


class FileParser(object):

    def __init__(self, fname):
        try:
            # Initialize Object
            self.infile = open(fname, 'r')

        except FileNotFoundError:
            print("File ", fname, " Not Found... Exiting")
            sys.exit()

    def __del__(self):
        # Close File
        if hasattr(self, 'file'):
            self.infile.close


class TrainingParser(FileParser):

    def __init__(self, fname):
        FileParser.__init__(fname)
        self.positiveWords = defaultdict(int)
        self.negativeWords = defaultdict(int)

    def __del__(self):
        FileParser.__del__()


class TestParser(FileParser):

    def __init__(self, fname):
        FileParser.__init__(fname)

    def __del__(self):
        FileParser.__del__()
