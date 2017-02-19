# Naive Bayes Classifier
# CS165A Machine Problem 1
# Lucas Lopilato

# import sys
from FileParser import *


class NaiveBayesClassifier(object):
    def __init__(self):
        # TODO Remove
        # Parse Command Line Arguments
        # args = str(sys.argv)
        """ if(len(args) != 3):
        print("proper usage: python \
        NaiveBayesClassifier.py training.txt testing.txt")"""

        # Open FileParsers
        train = TrainingParser("input/training.txt")
        self.train = train.train
        self.rating = train.rating
        train.__del__

        # Build Naive Bayes Variables
        self.pdocs = 0  # Number of Positive Documents
        self.ndocs = 0  # Number of Negative Documents

        # Count Total Number of Documents
        for rat in self.rating:
            if rat == 0:
                self.ndocs += 1
            else:
                self.pdocs += 1

        # Parse Each Test
        test = TestParser("input/testing.txt")

        test.__del__



init = NaiveBayesClassifier()
