__author__ = 'lus'

class CloudyWords(object):
    def __init__(self, minWordLen = 4):
        """
        Default initializer
        """
        self.wordsHash = dict()
        self.minWordLength = minWordLen
        self.totalWordsCount = 0
        self.illegalSymbols = { '.', ',', ';', '?', '<', '>', '[', ']', '(', ')', '{', '}', '`', '~', '!' }

    def addWords(self, wordOrSentence):
        """
        Method will populate engine with words.
        """
        wLines = wordOrSentence.split(' ')
        for line in wLines:
            for isy in self.illegalSymbols:
                line = line.replace(isy, '')
            line = line.strip().lower()

            if len(line) > self.minWordLength:
                self.totalWordsCount += 1

                if self.wordsHash.has_key(line):
                    self.wordsHash[line] += 1
                else:
                    self.wordsHash[line] = 1

    def cloud(self):
        """
        Method will return a list of words sorted by popularity ( more popular first )
        """
        if len(self.wordsHash) > 0:
            result = list()
            for key, value in sorted(self.wordsHash.iteritems(), key = lambda (k, v) : (v, k), reverse = True):
                result.append(key)

            return result
        return None

    def reset(self):
        self.totalWordsCount = 0
        self.wordsHash.clear()