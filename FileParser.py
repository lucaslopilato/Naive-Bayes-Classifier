# fileParser.py
# Class Responsible for handling all file IO
# Extracts useful information relative to Machine Problem 1
import sys
import string
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

    # Returns Map of Word Count
    # If not or non precedes the word, the count is -1 for that instance
    def cleanse(s: str):
        count = defaultdict(int)

        s = ''.join(s.filter((string.ascii_lowercase + ' ').__contains__))
        return count




class TrainingParser(FileParser):

    def __init__(self, fname):
        FileParser.__init__(self, fname)
        self.positiveWords = defaultdict(int)
        self.negativeWords = defaultdict(int)

    def __del__(self):
        FileParser.__del__(self)


class TestParser(FileParser):

    def __init__(self, fname):
        FileParser.__init__(self, fname)

    def __del__(self):
        FileParser.__del__(self)
