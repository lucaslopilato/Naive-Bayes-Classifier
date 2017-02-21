# fileParser.py
# Class Responsible for handling all file IO
# Extracts useful information relative to Machine Problem 1

# Stop words located at http://xpo6.com/list-of-english-stop-words/
import string
from collections import defaultdict
from strop import rfind


class FileParser(object):

    def __init__(self, train, stop=False, stem=False):
        # Initialize Object

        # Word Counts Per Class
        self.positiveWords = defaultdict(int)
        self.positiveDocs = 0
        self.negativeWords = defaultdict(int)
        self.negativeDocs = 0
        # self.stop = set()
        # self.negation = set()
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
        '''with open('input/stop.txt', 'r') as bf:
            for word in bf:
                self.stop.add(word.lower().strip())'''

        # Initialize Negation Dictionary
        '''with open('input/negation.txt', 'r') as neg:
            for word in neg:
                self.negation.add(word.lower().strip())'''

        '''with open('input/stem.txt', 'r') as stem:
            for word in stem:
                self.stem.append(word.lower().strip())'''

    # Writes the Found Review into the dictionary targetWords
    def cleanse(self, review, targetWords):
        review = ''.join(c for c in review if c in
                         string.ascii_letters + string.whitespace)

        # Parse Each Word Found in the String
        for x in review.split():
            targetWords[x] += 1

            # Ignore Stop Words
            '''if x in self.stop:
                continue'''

            # Stemming
            ''' x = self.destem(x)
            if len(x) < 3:
                continue '''

            # Check for negation
            '''if x in self.negation:
                neg *= -1
                continue '''

            # Update the count for the word

    def getReviews(self, file):
        reviews = []
        with open(file, 'r') as f:
            for review in f:
                review = review.strip()
                reviews.append(self.cleanse(review))
        return reviews

    def getRatings(self, file):
        ratings = []
        with open(file, 'r') as f:
            for review in f:
                review = review.strip()
                ratings.append(int(review[-1:]))
        return ratings

    def destem(self, string):

        index = 0
        for stem in self.stem:
            index = rfind(string, stem)
            if(index != -1 and index + len(stem) == len(string)):
                return string[:index]

        return string
