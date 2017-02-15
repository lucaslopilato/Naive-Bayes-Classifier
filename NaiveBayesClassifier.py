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
        train = TrainingParser("training.txt")
        test = TestParser("testing.txt")
