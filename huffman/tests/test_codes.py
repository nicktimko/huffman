from __future__ import absolute_import, print_function

import collections
import unittest

import huffman

class TestCodebookGeneration(unittest.TestCase):

    def test_basic(self):
        output = huffman.codebook([('A', 2), ('B', 4), ('C', 1), ('D', 1)])
        expected = {'A': '10', 'B': '0', 'C': '110', 'D': '111'}

        self.assertEqual(output, expected)

    def test_counter(self):
        input_ = sorted(collections.Counter('man the stand banana man').items())

        output = huffman.codebook(input_)
        expected = {
            ' ': '111',
            'a': '10',
            'b': '0101',
            'd': '0110',
            'e': '11000',
            'h': '0100',
            'm': '0111',
            'n': '00',
            's': '11001',
            't': '1101',
         }

        self.assertEqual(output, expected)
