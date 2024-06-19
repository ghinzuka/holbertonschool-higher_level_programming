#!/usr/bin/python3
"""extends the built-in iterator """


class CountedIterator:
    """class"""
    def __init__(self, some_iterable):
        """initialize iterator and counter"""
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """return count"""
        return self.counter

    def __next__(self):
        """overide the next method"""
        try:
            i = next(self.iterator)
            self.counter += 1
            return i
        except StopIteration:
            raise StopIteration
