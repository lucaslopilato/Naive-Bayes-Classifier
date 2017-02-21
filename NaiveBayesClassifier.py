# Naive Bayes Classifier
# CS165A Machine Problem 1
# Lucas Lopilato

# System Imports
from sys import argv
from math import log10
from time import time
from collections import defaultdict

# Local Imports
from FileParser import *


class NaiveBayesClassifier(object):

    def __init__(self,
                 training="input/training.txt",
                 testing="input/testing.txt"):

        # Train
        traint = time()
        self.train = FileParser(training)
        traint = time() - traint

        # Calculate Probability Of Each Class
        total = float(self.train.positiveDocs + self.train.negativeDocs)
        self.positive = self.train.positiveDocs / total
        self.negative = self.train.negativeDocs / total

        # Test Against Testing Set
        testt = time()
        trainAcc = self.test(testing, True)
        testt = time() - testt

        # Print Results
        print("%d seconds (training)" % traint)
        print("%d seconds (testing)" % testt)

        # Test and Print Results against training set
        print("%0.3f (training)" % self.test(training))
        print("%0.3f (testing)" % trainAcc)

    # Run a file against the algorithm
    def test(self, file, pr=False):
        # Initialize Testing Variables
        correct = 0.0  # Number Correct
        total = 0.0  # Number Total
        expected = -1  # Expected Value for a test
        actual = -1  # Actual Value for a test

        # Get Tests To Run
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

                # Print If Needed
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
    if len(argv) != 3:
        print('Usage: python NaiveBayesClassifier.py training.txt testing.txt')
        exit(1)

    init = NaiveBayesClassifier(argv[1], argv[2])
