from __future__ import absolute_import, print_function


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


def popper(heap):
    while heap:
        yield heap.pop()
