# Naive Bayes Classifier
# CS165A Machine Problem 1
# Lucas Lopilato

# import sys
from collections import defaultdict
from FileParser import *
import time


class NaiveBayesClassifier(object):

    def buildTotalClasses(self):
        for i in range(0, len(self.rating)):
            for word in self.train[i]:
                if(self.rating[i] == 0):
                    if word in self.negative:
                        self.negative[word] += self.train[i][word]
                    else:
                        self.negative[word] = 0
                else:
                    if word in self.positive:
                        self.positive[word] += self.train[i][word]
                    else:
                        self.positive[word] = 0

    def __init__(self, training="input/training.txt", testing="input/testing.txt"):
        # TODO Remove
        # Parse Command Line Arguments
        # args = str(sys.argv)
        """ if(len(args) != 3):
        print("proper usage: python \
        NaiveBayesClassifier.py training.txt testing.txt")"""
        # Begin Timing

        traint = time.time()

        # Open FileParsers
        train = FileParser()
        self.train = train.getReviews(training)
        self.rating = train.getRatings(training)

        # Build Total Class Dictionary
        self.positive = defaultdict(int)
        self.negative = defaultdict(int)
        self.buildTotalClasses()

        # End Timing and Print
        traint = time.time() - traint

        testt = time.time()
        self.expected = train.getRatings(testing)
        self.actual = []
        for test in train.getReviews(testing):
            self.actual.append(self.guess(test))
            print(str(self.actual[-1]))

        testt = time.time() - testt

        print("%0.3f (testing)" % self.accuracy(self.expected, self.actual))
        print("%1f seconds (training)" % traint)
        print("%1f seconds (testing)" % testt)

    # Returns Probabililty of Word Given Class
    def probGivenClass(self, review, word, given, alpha=0):
        try:
            return float(review[word] + alpha) / float(given[word] + alpha)
        except:
            return 0

    def accuracy(self, expected, actual):
        correct = 0
        for i in range(0, len(expected)):
            if(expected[i] == actual[i]):
                correct += 1

        return float(correct) / len(expected)

    # Guess the class of the review
    def guess(self, review):

        for word in review:
            try:
                pass
            try:
            except:
                pass
            # except:
            #     continue

        if pos > neg:
            return 1
        else:
            return 0





init = NaiveBayesClassifier()
