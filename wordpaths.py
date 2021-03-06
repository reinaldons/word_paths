#!/usr/bin/python

import argparse

from wp.exceptions import WordSizeException, WordNotInWordListException, ImpossiblePathException
from wp.main import WordPath


def run(first_word, last_word):
    word_path = WordPath()
    word_path.load_word_list('/usr/share/dict/words', len(first_word))

    try:
        chain = word_path.find(first_word, last_word)
        print(' > '.join(chain))
    except WordNotInWordListException as e:
        print('{}. Ensure both words exists in the words file.'.format(e))
    except (WordSizeException, ImpossiblePathException) as e:
        print('{}.'.format(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('first_word')
    parser.add_argument('last_word')
    args = parser.parse_args()

    run(args.first_word, args.last_word)
