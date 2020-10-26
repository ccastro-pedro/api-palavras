"""
Teste unitário da classe Words e de seus módulos.
"""

import unittest
from classes import *
import os


class TestWords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.words = Words()

        filenames = ['texto1.txt', 'texto2.txt', 'texto3.txt']

        cls.files = [os.path.join(os.getcwd(), f) for f in filenames]

        cls.unique_vocab = ['falar', 'é', 'fácil', 'mostre', 'código', 'escrever', 'difícil', 'funcione', 'oi1', 'ra2', 'este', 'melhor', 'facil',  'a41', 'a2']

        cls.two_gram_vocab = ['falar é', 'é fácil', 'fácil mostre', 'mostre código', 'fácil escrever', 'escrever código', 'código difícil', 'difícil é', 'é escrever',
                              'código funcione', 'oi1 ra2', 'ra2 este', 'este é', 'é melhor', 'melhor fácil', 'fácil facil', 'facil é', 'é facil', 'fácil a41', 'a41 a2']

        cls.num_unique = {'texto1.txt': [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                          'texto2.txt': [[0, 2, 1, 0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0]],
                          'texto3.txt': [[0, 3, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1]]}

        cls.num_two_gram = {'texto1.txt': [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                            'texto2.txt': [[0, 1, 0, 0, 1, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                            'texto3.txt': [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]]}

    def test_class_words(self):
        for file in self.files:
            self.words.add_files(file)
        self.assertEqual(self.words.files, self.files, f"Deveria ser {self.files}")

    def test_unique_vocab(self):
        self.assertEqual(self.words.unique_vocab, self.unique_vocab, f"Deveria ser {self.unique_vocab}")

    def test_two_gram_vocab(self):
        self.assertEqual(self.words.two_gram_vocab, self.two_gram_vocab, f"Deveria ser {self.two_gram_vocab}")

    def test_num_unique(self):
        self.assertEqual(self.words.num_unique, self.num_unique, f"Deveria ser {self.num_unique}")

    def test_num_two_gram(self):
        self.assertEqual(self.words.num_two_gram, self.num_two_gram, f"Deveria ser {self.num_two_gram}")

if __name__ == '__main__':
    unittest.main()