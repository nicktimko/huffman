huffman
=======

Generate Huffman codebooks! `Huffman codes`_ are the optimal way to compress individual symbols into a binary sequence that can be unambiguously decoded without inter-symbol separators (it is "`prefix-free`_").

Provided an iterable of 2-tuples in ``(symbol, weight)`` format, generate a Huffman codebook, returned as a dictionary in ``{symbol: code, ...}`` format.

::

    >>> huffman.codebook([('A', 2), ('B', 4), ('C', 1), ('D', 1)])
    {'A': '10', 'B': '0', 'C': '110', 'D': '111'}

If you have an iterable of symbols, the ``collections.Counter`` is a handy way to tally them up.

::

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


.. _Huffman codes: https://en.wikipedia.org/wiki/Huffman_coding
.. _prefix-free: https://en.wikipedia.org/wiki/Prefix_code
