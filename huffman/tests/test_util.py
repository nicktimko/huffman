from __future__ import absolute_import, print_function

import random
import unittest

from .util import is_sorted, popper

class TestIsSorted(unittest.TestCase):

    def test_is_sorted(self):
        assert is_sorted([1])
        assert is_sorted([1, 2])
        assert is_sorted([1, 2, 3])
        assert is_sorted([1, 2, 2])
        assert is_sorted([2, 2, 2])
        assert is_sorted([])
        assert is_sorted((1, 2, 3))
        assert is_sorted('abc')
        assert is_sorted('123')
        assert is_sorted('eggs')
        assert is_sorted(iter([1, 2, 3]))

    def test_is_not_sorted(self):
        assert not is_sorted([3, 2, 1])
        assert not is_sorted([2, 2, 1])
        assert not is_sorted('spam')


class TestPopper(unittest.TestCase):

    def test_popper(self):
        for i in range(10):
            x = list(range(i))

            j = 0
            for _ in popper(x):
                j += 1

            self.assertEqual(i, j)
