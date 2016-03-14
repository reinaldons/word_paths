
from .exceptions import WordSizeException, WordNotInWordList


class WordPath:

    def __init__(self):
        self.word_list = []
        self.chain = []

    def load_word_list(self, file_path, word_size):
        with open(file_path) as file:
            self.word_list = [line.strip().lower() for line in file if len(line.strip()) == word_size]

    def in_word_list(self, word):
        return word in self.word_list

    def is_valid_diff(self, word1, word2):
        """
        Both words can only have 1 different letter
        """
        count = 0
        for a, b in zip(word1, word2):
            if a != b:
                count += 1
                if count > 1:
                    return False

        return count == 1

    def populate_chain(self, first_word, last_word):
        for word in self.word_list:
            if self.is_valid_diff(word1=word, word2=first_word) and word not in self.chain:
                self.chain.append(word)
                if word == last_word:
                    return
                self.populate_chain(first_word=word, last_word=last_word)

    def find(self, first_word, last_word):
        if len(first_word) != len(last_word):
            raise WordSizeException('Words should have the same size')

        if not self.in_word_list(first_word):
            raise WordNotInWordList('Word {} not in the word list'.format(first_word))

        if not self.in_word_list(last_word):
            raise WordNotInWordList('Word {} not in the word list'.format(last_word))

        self.chain.append(first_word)
        self.populate_chain(first_word, last_word)

        return self.chain
