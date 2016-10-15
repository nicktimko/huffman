from __future__ import print_function

import sys
import random
import unittest

if sys.version_info >= (2, 7):
    from collections import Counter
else:
    Counter = None
    def next(i):
        return i.next()

import huffman
from huffman.heapqo import Heap


def assertEqualDicts(a, b):
    a = set(a.items())
    b = set(b.items())

    excess_a = a - b
    excess_b = b - a

    if excess_a or excess_b:

        print('First dictionary has extra items not in second (+) or missing from second (-)', file=sys.stderr)
        for sign, items in [('+', excess_a), ('-', excess_b)]:
            for item in sorted(items):
                print('({}) {}'.format(sign, item), file=sys.stderr)

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


def is_sorted(i):
    i = iter(i)
    try:
        a = next(i)
    except StopIteration:
        # zero length iterable
        return True
    for b in i:
        if a > b:
            return False
    return True


def test_is_sorted():
    assert is_sorted([1])
    assert is_sorted([1, 2])
    assert is_sorted([1, 2, 3])
    assert is_sorted([1, 2, 2])
    assert is_sorted([2, 2, 2])
    assert is_sorted([])
    assert is_sorted((1, 2, 3))
    assert is_sorted('123')
    assert is_sorted('abc')
    assert is_sorted(iter([1, 2, 3]))
    assert not is_sorted([3, 2, 1])
    assert not is_sorted([2, 2, 1])


def popper(heap):
    while heap:
        yield heap.pop()


def test_heap_pops_always_sorted():
    for _ in range(500):
        nums = [random.randrange(10) for _ in range(random.randrange(1, 10))]
        heap = Heap(nums)
        assert is_sorted(popper(heap))


def test_heap_pushpops_always_min():
    for _ in range(10):
        nums = [random.randrange(10) for _ in range(random.randrange(1, 10))]
        heap = Heap(nums)
        for _ in range(500):
            in_ = random.randrange(-5, 15)
            lo = min(min(heap.heap), in_)
            out = heap.pushpop(in_)
            assert out == lo


def test_heap_replace():
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


def test_heap_complain_unorderable():
    if sys.version_info < (3,):
        raise unittest.SkipTest('Python 2 happily compares disparate types.')

    heap = Heap([1, 2, 3])
    try:
        heap.push([])
    except ValueError as e:
        assert 'order' in str(e)
    else:
        assert False, 'allowed insertion of unorderable type'


def test_heap_post_push_unorderable_not_broken():
    heap = Heap([1, 2, 3])
    try:
        heap.push([])
    except ValueError:
        pass
    else:
        pass

    heap.pop() # this should run fine and not see that list or Python 2 won't care
