# fileParser.py
# Class Responsible for handling all file IO
# Extracts useful information relative to Machine Problem 1

# Stop words located at http://xpo6.com/list-of-english-stop-words/
import string
from collections import defaultdict
from strop import rfind


class Trainer(object):

    def __init__(self, train, stop=False, stem=False):
        # Initialize Object

        # Word Counts Per Class
        self.positiveWords = defaultdict(int)
        self.positiveDocs = 0
        self.negativeWords = defaultdict(int)
        self.negativeDocs = 0
        self.stop = set()
        # self.stem = []

        # Train the dataset
        with open(train, 'r') as training:
            for review in training:
                review = review.strip().lower()
                if review[-1] == '1':
                    self.positiveDocs += 1
                    self.cleanse(review, self.positiveWords)
                elif review[-1] == '0':
                    self.negativeDocs += 1
                    self.cleanse(review, self.negativeWords)
                else:
                    print('BAD REVIEW: %s' % review)
                    raise ValueError('Error... rating could not be parsed')

        # Initialize Blacklist
        if stop:
            with open('input/stop.txt', 'r') as bf:
                for word in bf:
                    self.stop.add(word.lower().strip())

        '''with open('input/stem.txt', 'r') as stem:
            for word in stem:
                self.stem.append(word.lower().strip())'''

    # Writes the Found Review into the dictionary targetWords
    def cleanse(self, review, targetWords):
        review = ''.join(c for c in review if c in
                         string.ascii_letters + string.whitespace)

        # Parse Each Word Found in the String
        for x in review.split():

            # Ignore Stop Words
            if x in self.stop:
                continue

            targetWords[x] += 1


            # Stemming
            ''' x = self.destem(x)
            if len(x) < 3:
                continue '''


    def destem(self, string):

        index = 0
        for stem in self.stem:
            index = rfind(string, stem)
            if(index != -1 and index + len(stem) == len(string)):
                return string[:index]

        return string
