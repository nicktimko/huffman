from __future__ import print_function

import sys
if sys.version_info >= (2, 7):
    from collections import Counter
else:
    Counter = None

import huffman


def assertEqualDicts(a, b):
    a = set(a.items())
    b = set(b.items())

    excess_a = a - b
    excess_b = b - a

    if excess_a or excess_b:

        print('First dictionary has extra items not in second (+) or missing from second (-)', file=sys.stderr)
        for sign, items in [('+', excess_a), ('-', excess_b)]:
            for item in sorted(items):
                print('({0}) {1}'.format(sign, item), file=sys.stderr)

        raise AssertionError('Dictionaries dissimilar')


def test_basic():
    output = huffman.codebook([('A', 2), ('B', 4), ('C', 1), ('D', 1)])
    expected = {'A': '10', 'B': '0', 'C': '110', 'D': '111'}

    assertEqualDicts(output, expected)


def test_counter():
    if Counter:
        input = sorted(Counter('man the stand banana man').items())
    else:
        input = [(' ', 4), ('a', 6), ('b', 1), ('d', 1), ('e', 1),
                 ('h', 1), ('m', 2), ('n', 5), ('s', 1), ('t', 2)]

    output = huffman.codebook(input)
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

    assertEqualDicts(output, expected)
