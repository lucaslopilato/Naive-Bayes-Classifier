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
            self.blacklist = set()

            # Initialize Blacklist
            with open('blacklist.txt', 'r') as bf:
                for word in bf:
                    self.blacklist.add(word.lower().strip())

        except FileNotFoundError:
            print("File ", fname, " Not Found... Exiting")
            sys.exit()

    def __del__(self):
        # Close File
        if hasattr(self, 'infile'):
            self.infile.close

    # Returns Map of Word Count
    # If not or non precedes the word, the count is -1 for that instance
    @staticmethod
    def cleanse(s: str):
        count = defaultdict(int)

        s = ''.join(filter((string.ascii_lowercase + ' ').__contains__, s))
        s = s.split()

        # Parse Each Word Found in the String
        for x in s:
            # Ignore 1 length words
            if(len(x) > 1):
                continue
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
