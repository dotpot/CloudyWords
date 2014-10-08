from collections import defaultdict


class CloudyWords(object):
    def __init__(self, min_word_len=4):
        """
        Default initializer, min_word_len is default minimal length of the word which will be added to the tree.
        """
        self.weight = defaultdict(int)
        self.min_word_length = min_word_len
        self.illegal_symbols = {'.', ',', ';', '?', '<', '>', '[', ']', '(', ')', '{', '}', '`', '~', '!'}

    def add_words(self, word_or_sentence):
        """
        Method will populate engine with words.
        """
        w_lines = word_or_sentence.split(' ')
        for line in map(str.lower, map(str.strip, w_lines)):
            for isy in self.illegal_symbols:
                line = line.replace(isy, '')

            if len(line) > self.min_word_length:
                self.weight[line] += 1

    def cloud(self):
        """
        Method will return a list of words sorted by popularity ( more popular goes first )
        """
        if len(self.weight) > 0:
            result = list()
            for key, value in sorted(self.weight.iteritems(), key=lambda (k, v): (v, k), reverse=True):
                result.append(key)
            return result
        return None

    def total_words_count(self):
        """ Returns total words count. """
        return len(self.weight)

    def reset(self):
        """ Cleans up. """
        self.weight.clear()
