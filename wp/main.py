
from .exceptions import WordSizeException, WordNotInWordListException, ImpossiblePathException


class WordPath:

    def __init__(self):
        self.word_list = []
        self.chain = []
        self.complete_chain = False

    def load_word_list(self, file_path, word_size):
        with open(file_path) as file:
            self.word_list = [line.strip().lower() for line in file if len(line.strip()) == word_size]

    def in_word_list(self, word):
        return word in self.word_list

    def is_valid_diff(self, word1, word2):
        """
        Should have just 1 different letter between them
        """
        count = 0
        for a, b in zip(word1, word2):
            if a != b:
                count += 1
                if count > 1:
                    return False

        return count == 1

    def populate_chain(self, first_word, last_word):
        slice_index = self.word_list.index(first_word)
        temp_word_list = self.word_list[slice_index:]  # slice to just look forward
        word1 = first_word
        for word in temp_word_list:
            if self.is_valid_diff(word1=word1, word2=word) and word not in self.chain:
                self.chain.append(word)
                if word == last_word:
                    self.complete_chain = True
                    return
                word1 = word

    def find(self, first_word, last_word):
        if len(first_word) != len(last_word):
            raise WordSizeException('Words should have the same size')

        if not self.in_word_list(first_word):
            raise WordNotInWordListException('Word {} not in the word list'.format(first_word))

        if not self.in_word_list(last_word):
            raise WordNotInWordListException('Word {} not in the word list'.format(last_word))

        self.chain.append(first_word)
        self.populate_chain(first_word, last_word)

        if not self.complete_chain:
            raise ImpossiblePathException('{} and {} have no viable path between them'.format(first_word, last_word))

        return self.chain
