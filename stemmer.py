

# Implements Porter stemming algorithm
# Assumes all input strings are lower case and cleaned using 'cleanse'
class stemmer(object):

    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def isVowel(self, word, index):
        letter = word[index]
        if(index == 0):
            letterBefore = ''
        else:
            letterBefore = word[index - 1]

        if letter in self.vowels:
            return True
        if letter == 'y':
            if letterBefore == '':
                return False
            elif letterBefore not in self.vowels:
                return True
            else:
                return False
        return False

    # Find the measure of given string
    def measure(self, word):
        measure = 0

        i = 0
        # Removing Beginning Consonants
        while(i < len(word)):
            if not self.isVowel(word, i):
                i += 1
            else:
                break


        # Calculate Measure
        while(i < len(word) and (i + 1) < len(word)):
            if(self.isVowel(word, i) and not self.isVowel(word, i + 1)):
                measure += 1
            i += 1

        return measure

    def containsVowel(self, word):
        for i in range (0, len(word)):
            if self.isVowel(word, i):
                return True

        return False

    def doubleConst(self, word):
        length = len(word)
        if length < 2:
            return False
        if not self.isVowel(word, length - 1) and not self.isVowel(word, length - 2):
            return True
        else:
            return False

    # Follows Porter Algorithm shown at 
    # http://snowball.tartarus.org/algorithms/porter/stemmer.html
    def stem(self, word):
        word = self.stepone(word)

        return word

    def stepone(self, word):
        # 1a
        if(word[-4:] == 'sses'):
            word = word[:-4] + 'ss'
        elif(word[-3:] == 'ies'):
            word = word[:-3] + 'i'
        elif(word[-2:] == 'ss'):
            word = word[:-2] + 'ss'
        elif(word[-1:] == 's'):
            word = word[:-1]

        # 1b
        if word[-3:] == 'eed':
            if self.measure(word[:-3]) > 0:
                word = word[:-3] + 'ee'
        elif word[-2:] == 'ed':
            if self.containsVowel(word[:-2]):
                word = word[:-2]
        elif word[-3:] == 'ing' and self.containsVowel(word[:-3]):
            word = word[:-3]

        return word


    # Only executed if step 2 or 3 of step 1b is successful
    def steponesub(self, word):
        if word[-2:] == 'at':
            word = word[:-2] + 'ate'
        elif word[-2:] == 'bl':
            word = word[:-2] + 'ble'
        elif word[-2:] == 'iz':
            word = word[:-2] + 'ize'
