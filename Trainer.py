# fileParser.py
# Class Responsible for handling all file IO
# Extracts useful information relative to Machine Problem 1

# Stop words located at http://xpo6.com/list-of-english-stop-words/
import string
from collections import defaultdict
from strop import rfind
from stemmer import stemmer


class Trainer(object):

    def __init__(self, train, stop=False, stem=False):
        # Initialize Object

        # Word Counts Per Class
        self.positiveWords = defaultdict(int)
        self.positiveDocs = 0
        self.negativeWords = defaultdict(int)
        self.negativeDocs = 0
        self.totalPositiveWords = 0.0
        self.totalNegativeWords = 0.0
        self.stop = set()
        if stem:
            self.stem = stemmer()
        else:
            self.stem = None

        # Train the dataset
        with open(train, 'r') as training:
            for review in training:
                review = review.strip().lower()
                if review[-1] == '1':
                    self.positiveDocs += 1
                    self.cleanse(review, self.positiveWords, self.totalPositiveWords)
                elif review[-1] == '0':
                    self.negativeDocs += 1
                    self.cleanse(review, self.negativeWords, self.totalNegativeWords)
                else:
                    pass

        # Initialize Blacklist
        if stop:
            with open('input/stop.txt', 'r') as bf:
                for word in bf:
                    self.stop.add(word.lower().strip())

    # Writes the Found Review into the dictionary targetWords
    def cleanse(self, review, targetWords, targetCount=None):
        review = ''.join(c for c in review if c in
                         string.ascii_letters + string.whitespace)

        # Parse Each Word Found in the String
        for x in review.split():

            # Ignore Stop Words
            if x in self.stop:
                continue

            if(self.stem is not None):
                x = self.stem.stem(x)

            if(targetCount is not None):
                targetCount += 1
            targetWords[x] += 1
