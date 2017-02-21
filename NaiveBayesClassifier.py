# Naive Bayes Classifier
# CS165A Machine Problem 1
# Lucas Lopilato

# import sys
from collections import defaultdict
from FileParser import *
import time
from math import log10


class NaiveBayesClassifier(object):

    def __init__(self,
                 training="input/training.txt",
                 testing="input/testing.txt"):
        # TODO Remove
        # Parse Command Line Arguments
        # args = str(sys.argv)
        """ if(len(args) != 3):
        print("proper usage: python \
        NaiveBayesClassifier.py training.txt testing.txt")"""
        # Begin Timing

        # Train
        traint = time.time()
        self.train = FileParser(training)
        traint = time.time() - traint

        # Calculate Probability Of Each Class
        total = float(self.train.positiveDocs + self.train.negativeDocs)
        self.positive = self.train.positiveDocs / total
        self.negative = self.train.negativeDocs / total

        # Test Against Testing Set
        testt = time.time()
        trainAcc = self.test(testing, True)
        testt = time.time() - testt

        print("%0.3f (training)" % self.test(training))
        print("%0.3f (testing)" % trainAcc)
        print("%1f seconds (training)" % traint)
        print("%1f seconds (testing)" % testt)

    # Run a full test
    def test(self, file, pr=False):
        # Initialize Testing Variables
        correct = 0.0
        total = 0.0
        expected = -1
        actual = -1

        # Test Training Against Itself
        with open(file, 'r') as tests:
            for review in tests:
                # Count Total Tests
                total += 1.0

                # Reset Words for the Review
                words = defaultdict(int)
                review = review.strip().lower()
                expected = int(review[-1])  # Get Expected
                self.train.cleanse(review, words)  # Read In Review's Words
                actual = self.guess(words)  # Guess Based on Words

                if pr:
                    print(actual)

                # Check Results
                if actual == expected:
                    correct += 1.0

        return (correct / total)

    # Guess the class of the set of words
    def guess(self, words):
        positive = log10(self.positive)
        negative = log10(self.negative)

        for word in words:
            try:
                positive += log10(self.train.positiveWords[word])
            except:
                pass
            try:
                negative += log10(self.train.negativeWords[word])
            except:
                pass

        if positive > negative:
            return 1
        else:
            return 0


if __name__ == '__main__':
    init = NaiveBayesClassifier()
