
import unittest
from unittest import mock

from wp.exceptions import WordSizeException, WordNotInWordListException, ImpossiblePathException
from wp.main import WordPath


def create_mock_open(file_text):
    # mock_open does not implement iteration on return object as 'open' do
    m_open = mock.mock_open(read_data=file_text)
    m_open.return_value.__iter__ = lambda self: self
    m_open.return_value.__next__ = lambda self: self.readline()

    return m_open


class TestWordPath(unittest.TestCase):

    def test_load_word_list(self):
        """
        Ensure that file data is loaded into a list with one word per list position
        """
        expected_dict = ['first', 'third']
        file_text = '\n'.join(expected_dict + ['five'])

        word_path = WordPath()
        with mock.patch('wp.main.open', create_mock_open(file_text=file_text)):
            word_path.load_word_list('test', 5)

        self.assertListEqual(expected_dict, word_path.word_list)

    def test_word_in_word_list(self):
        """
        WordPath.in_word_list should return True if given word exists in WordPath.word_list
        """
        word_path = WordPath()
        with mock.patch('wp.main.open', create_mock_open(file_text='\n'.join(['one', 'two', 'three']))):
            word_path.load_word_list('test', 3)

        self.assertTrue(word_path.in_word_list('two'))

    def test_word_not_in_word_list(self):
        """
        WordPath.in_word_list should return False if given word not exists in WordPath.word_list
        """
        word_path = WordPath()
        with mock.patch('wp.main.open', create_mock_open(file_text='\n'.join(['one', 'two', 'three']))):
            word_path.load_word_list('test', 3)

        self.assertFalse(word_path.in_word_list('four'))

    def test_find_word_size_verification(self):
        """
        Ensure that find method throw an exception if words have different size
        """
        word_path = WordPath()

        with self.assertRaises(WordSizeException):
            word_path.find('123', '1234')

    def test_find_with_first_word_not_in_word_list(self):
        """
        Ensure that find method throw an exception if first word is not present on WordPath.word_list
        """
        word_path = WordPath()
        with mock.patch('wp.main.open', create_mock_open(file_text='\n'.join(['one', 'two', 'three']))):
            word_path.load_word_list('test', 3)

        with self.assertRaises(WordNotInWordListException):
            word_path.find('two', 'six')

    def test_find_with_last_word_not_in_word_list(self):
        """
        Ensure that find method throw an exception if last word is not present on WordPath.word_list
        """
        word_path = WordPath()
        with mock.patch('wp.main.open', create_mock_open(file_text='\n'.join(['one', 'two', 'three']))):
            word_path.load_word_list('test', 3)

        with self.assertRaises(WordSizeException):
            word_path.find('one', 'four')

    def test_populate_chain(self):
        """
        Ensure that populate_chain method return the expected dict
        """
        expected_dict = ['cat', 'cag', 'cog', 'dog']
        file_text = '\n'.join(expected_dict + ['fog', 'zog'])

        word_path = WordPath()
        with mock.patch('wp.main.open', create_mock_open(file_text=file_text)):
            word_path.load_word_list('test', 3)

        word_path.chain.append('cat')
        word_path.populate_chain('cat', 'dog')
        self.assertListEqual(expected_dict, word_path.chain)

    def test_find_with_no_viable_path(self):
        """
        Ensure that find method raise an Exception when have no viable path between given words
        """
        file_text = '\n'.join(['aaa', 'cat', 'cog', 'dog', 'fog', 'zog'])

        word_path = WordPath()
        with mock.patch('wp.main.open', create_mock_open(file_text=file_text)):
            word_path.load_word_list('test', 3)

        with self.assertRaises(ImpossiblePathException):
            word_path.find('cat', 'dog')

    def test_find_with_viable_path(self):
        """
        Ensure that find method return the expected dict
        """
        expected_dict = ['cat', 'cag', 'cog', 'dog']
        file_text = '\n'.join(['aaa', 'cat', 'cag', 'cog', 'caf', 'dog', 'fog', 'zog'])

        word_path = WordPath()
        with mock.patch('wp.main.open', create_mock_open(file_text=file_text)):
            word_path.load_word_list('test', 3)

        self.assertListEqual(expected_dict, word_path.find('cat', 'dog'))
