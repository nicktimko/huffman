from __future__ import absolute_import, print_function

import sys
import random
import unittest

from huffman.heapqo import Heap

from .util import is_sorted, popper


class TestHeapPopAlwaysSorted(unittest.TestCase):

    def test_heap_pops_always_sorted(self):
        for _ in range(500):
            nums = [random.randrange(10) for _ in range(random.randrange(1, 10))]
            heap = Heap(nums)
            assert is_sorted(popper(heap))

    def test_heap_pushpops_always_min(self):
        for _ in range(10):
            nums = [random.randrange(10) for _ in range(random.randrange(1, 10))]
            heap = Heap(nums)
            for _ in range(500):
                in_ = random.randrange(-5, 15)
                lo = min(min(heap.heap), in_)
                out = heap.pushpop(in_)
                assert out == lo

    def test_heap_replace(self):
        """
        similar to pushpop, but won't return input if that's lower. basically
        a pop-push
        """
        for _ in range(10):
            nums = [random.randrange(10) for _ in range(random.randrange(1, 10))]
            heap = Heap(nums)
            for _ in range(500):
                in_ = random.randrange(-5, 15)
                lo = min(heap.heap)
                out = heap.replace(in_)
                assert out == lo


class TestHeapOrderableItems(unittest.TestCase):

    def test_heap_complain_unorderable(self):
        if sys.version_info < (3,):
            raise unittest.SkipTest('Python 2 happily compares disparate types.')

        heap = Heap([1, 2, 3])
        try:
            heap.push([])
        except ValueError as e:
            self.assertIn('order', str(e))
        else:
            self.fail('allowed insertion of unorderable type')

    def test_heap_post_push_unorderable_not_broken(self):
        heap = Heap([1, 2, 3])
        try:
            heap.push([])
        except ValueError:
            pass
        else:
            pass

        for x in popper(heap):
            pass # this should run fine and not see that list or Python 2 won't care
