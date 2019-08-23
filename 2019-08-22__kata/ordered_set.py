from collections import OrderedDict, MutableSet


class OrderedSet(OrderedDict, MutableSet):
    # For this to be a true class, you should implement all the set functions __le__, __lt__, add, discard, etc.
    def __init__(self, *args):
        for arg in args:
            for element in arg:
                self[element] = None

    def __str__(self):
        return ' '.join(self.keys())
