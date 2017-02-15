# fileParser.py
# Class Responsible for handling all file IO
# Extracts useful information relative to Machine Problem 1
import sys
import string


class FileParser(object):

    def __init__(self, fname):
        try:
            # Initialize Object
            self.infile = open(fname, 'r')
            self.blacklist = set()
            self.negation = set()

            # Initialize Blacklist
            with open('input/blacklist.txt', 'r') as bf:
                for word in bf:
                    self.blacklist.add(word.lower().strip())

            # Initialize Negation Dictionary
            with open('input/negation.txt', 'r') as neg:
                for word in neg:
                    self.negation.add(word.lower().strip())

        except FileNotFoundError:
            print("File ", fname, " Not Found... Exiting")
            sys.exit()

    def __del__(self):
        # Close File
        if hasattr(self, 'infile'):
            self.infile.close

    # Returns Map of Word Count
    # If not or non precedes the word, the count is -1 for that instance
    def cleanse(self, s: str):
        count = {}

        s = ''.join(c.lower() for c in s if c in string.ascii_letters + ' ')
        s = s.split()

        # Detects whether negation detected
        neg = 1

        # Parse Each Word Found in the String
        for x in s:
            # Ignore 1 length words
            if(len(x) <= 1):
                continue

            # Check for negation
            if x in self.negation:
                neg *= -1
                continue

            # Update the count for the word
            if x in count:
                count[x] += neg
            else:
                count[x] = neg

            # Reset Negation
            neg = 1 
        return count


class TrainingParser(FileParser):

    def __init__(self, fname):
        FileParser.__init__(self, fname)


    def __del__(self):
        FileParser.__del__(self)


class TestParser(FileParser):

    def __init__(self, fname):
        FileParser.__init__(self, fname)

    def __del__(self):
        FileParser.__del__(self)
