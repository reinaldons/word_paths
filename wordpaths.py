#!/usr/bin/python

import argparse

from wp.main import WordPath


def run(first_word, last_word):
    word_path = WordPath()
    word_path.load_word_list('tests/functional/misc/words', len(first_word))
    chain = word_path.find(first_word, last_word)

    print(' > '.join(chain))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('first_word')
    parser.add_argument('last_word')
    args = parser.parse_args()

    run(args.first_word, args.last_word)
