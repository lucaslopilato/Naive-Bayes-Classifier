# fileParser.py
# Class Responsible for handling all file IO
# Extracts useful information relative to Machine Problem 1

# Stop words located at http://xpo6.com/list-of-english-stop-words/
import string
from collections import defaultdict
from strop import rfind


class FileParser(object):

    def __init__(self):
        # Initialize Object
        self.stop = set()
        self.negation = set()
        self.stem = []

        # Initialize Blacklist
        with open('input/stop.txt', 'r') as bf:
            for word in bf:
                self.stop.add(word.lower().strip())

        # Initialize Negation Dictionary
        with open('input/negation.txt', 'r') as neg:
            for word in neg:
                self.negation.add(word.lower().strip())

        with open('input/stem.txt', 'r') as stem:
            for word in stem:
                self.stem.append(word.lower().strip())

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

    # Returns Map of Word Count
    # If not or non precedes the word, the count is -1 for that instance
    def cleanse(self, s):
        count = defaultdict(int)

        s = ''.join(c for c in s.lower() if c in string.ascii_letters + ' ')

        # Detects whether negation detected
        neg = 1

        # Parse Each Word Found in the String
        for x in s.split():

            # Ignore Stop Words
            if x in self.stop:
                continue

            # Stemming
            x = self.destem(x)
            if len(x) < 3:
                continue

            # Check for negation
            '''if x in self.negation:
                neg *= -1
                continue '''

            # Update the count for the word
            if x in count:
                count[x] += neg
            else:
                count[x] = neg

            # Reset Negation
            # neg = 1
        return count
