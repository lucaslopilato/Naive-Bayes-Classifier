# Naive Bayes Classifier
# CS165A Machine Problem 1
# Lucas Lopilato

# System Imports
from sys import argv
from math import log10
from time import time
from collections import defaultdict

# Local Imports
from Trainer import *


class NaiveBayesClassifier(object):

    def __init__(self,
                 training="input/training.txt",
                 testing="input/testing.txt",
                 top10=False,
                 stop=False,
                 stem=False,
                 pbayes=True,
                 pmultiBayes=False,
                 pmissing=False):

        self.pbayes = pbayes
        self.pmultiBayes = pmultiBayes
        self.pmissing = pmissing
        self.top10 = top10

        # Train
        traint = time()
        self.train = Trainer(training, stop, stem)
        traint = time() - traint

        # Calculate Probability Of Each Class
        total = float(self.train.positiveDocs + self.train.negativeDocs)
        self.positive = self.train.positiveDocs / total
        self.negative = self.train.negativeDocs / total
        self.totalWords = float(len(self.train.positiveWords) + len(self.train.negativeWords))

        # Test Against Testing Set
        testt = time()
        trainAcc = self.test(testing, True)
        testt = time() - testt

        # Print Results
        print("%d seconds (training)" % traint)
        print("%d seconds (labeling)" % testt)

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
            top10 = {}
            for review in tests:
                # Count Total Tests
                total += 1.0

                # Reset Words for the Review
                words = defaultdict(int)
                review = review.strip().lower()
                try:
                    expected = int(review[-1])  # Get Expected
                    self.train.cleanse(review, words)  # Read In Review's Words
                    actual = self.guess(words)  # Guess Based on Words
                    if self.top10:
                        top10 = self.topTen(words, top10)
                except:
                    continue

                # Print If Needed
                if pr:
                    print(actual)

                # Check Results
                if actual == expected:
                    correct += 1.0

            if self.top10:
                print(top10)
        return (correct / total)

    # Guess Based on multiple algorithms
    def guess(self, words):
        total = self.pbayes + self.pmultiBayes + self.pmissing

        # Traditional Bayes Rule
        pos = 0.0

        if self.pbayes:
            pos += float(self.bayes(words))

        if self.pmultiBayes:
            # Laplace Smoothing
            if self.multinomialBayes(words) > 0:
                pos += 1

        if self.pmissing:
            pos += float(self.missing(words))

        if((pos / total) >= 0.5):
            return 1
        else:
            return 0

    # Simply Count which words are missing from the other set
    def missing(self, words):
        inPos = 0
        inNeg = 0
        for word in words:
            if word in self.train.positiveWords and word not in self.train.negativeWords:
                inPos += 1
            elif word not in self.train.positiveWords and worn in self.train.negativeWords:
                inNeg += 1

        if inPos >= inNeg:
            return 1
        else:
            return 0


    # Formula found at http://scikit-learn.org/stable/modules/naive_bayes.html
    def multinomialBayes(self, words, alpha=1):
        positive = log10(self.positive)
        negative = log10(self.negative)

        for word in words:
            try:
                pos = log10(self.train.positiveWords[word] + alpha)
                pos -= log10(self.train.totalPositiveWords + (alpha * len(self.train.positiveWords)))
                neg = log10(self.train.negativeWords[word] + alpha)
                neg -= log10(self.train.totalNegativeWords + (alpha * len(self.train.negativeWords)))
                positive += pos
                negative += neg
            except:
                continue

        return (positive - negative)

    def bayes(self, words):
        positive = log10(self.positive)
        negative = log10(self.negative)

        for word in words:
            # Calculate Total Occurrances of Word
            totalOfWord = float(self.train.positiveWords[word] + self.train.negativeWords[word])
            try:
                # P(Word | Positive)
                pos = (
                    log10(self.train.positiveWords[word]) - log10(totalOfWord))

                # P(Word)
                pos += (log10(totalOfWord) - log10(self.totalWords))

                # P(Positive)
                pos -= log10(self.positive)

                # P(Positive | Word) =
                # P(Word | Positive) * P(Word) / P(Positive)
                # P(Word | Negative)
                neg = (
                    log10(self.train.negativeWords[word]) - log10(totalOfWord))

                # P(Word)
                neg += (log10(totalOfWord) - log10(self.totalWords))

                # P(Negative)
                neg -= log10(self.negative)

                # P(Negative | Word) =
                # P(Word | Negative) * P(Word) / P(Negative)
                negative += neg
                positive += pos
            except:
                pass

        if positive > negative:
            return 1
        else:
            return 0

    def topTen(self, words, top10):
        for word in words:
            value = abs(self.multinomialBayes([word]))
            if len(top10) < 10:
                top10[word] = value
            else:
                sorted10 = sorted(top10.items(), key=operator.itemgetter(1))
                if value > sorted10[-1]:
                    top10.remove(sorted10[-1])
                    top10[word] = value

        return top10


if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage: python NaiveBayesClassifier.py training.txt testing.txt')
        exit(1)

    init = NaiveBayesClassifier(
        argv[1],
        argv[2].rstrip('\n\r'),
        top10=False,
        stop=False,
        stem=False,
        pbayes=True,
        pmultiBayes=False,
        pmissing=False)
