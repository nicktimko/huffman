from __future__ import print_function, absolute_import

from .heapqo import Heap

__all__ = ['Node', 'Leaf', 'Tree', 'codebook']


class Node(object):
    def __init__(self, left, right):
        self.parent = None
        left.parent = right.parent = self

        self.left = left
        self.right = right

        self.weight = left.weight + right.weight

    def __repr__(self):
        return '<Node with weight {}>'.format(self.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class Leaf(Node):
    def __init__(self, symbol, weight):
        self.parent = None
        self.symbol = symbol
        self.weight = weight

    def __repr__(self):
        return "<Leaf '{}' with weight {}, code '{}'>".format(self.symbol, self.weight, self.code)

    @property
    def code(self):
        code = ''
        n = self
        while n.parent is not None:
            codebit = '0' if n is n.parent.left else '1'
            code = codebit + code
            n = n.parent
        return code


class Tree(object):
    def __init__(self, symbolweights):
        leaves = [Leaf(*sw) for sw in symbolweights]
        heap = Heap(leaves[:])

        while len(heap) >= 2:
            heap.push(Node(heap.pop(), heap.pop()))

        self.root = heap.pop()
        self.codebook = {l.symbol: l.code for l in leaves}


def codebook(symbolweights):
    '''
    Provided an iterable of 2-tuples in (symbol, weight) format, generate a
    Huffman codebook, returned as a dictionary in {symbol: code} format.

    Examples:
    >>> huffman.codebook([('A', 2), ('B', 4), ('C', 1), ('D', 1))
    {'A': '10', 'B': '0', 'C': '110', 'D': '111'}

    >>> huffman.codebook(collections.Counter('man the stand banana man').items())
    {' ': '111',
     'a': '10',
     'b': '0100',
     'd': '0110',
     'e': '11010',
     'h': '0101',
     'm': '1100',
     'n': '00',
     's': '11011',
     't': '0111'}
    '''
    return Tree(symbolweights).codebook
