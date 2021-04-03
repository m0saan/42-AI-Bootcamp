import numpy as np


class NumPyCreator:
    """This the class representation of NumPyCreator. a class that gets a different types of data structure and
    transforms it into a NumPy array: """

    def __init__(self):
        pass

    def from_list(self, lst: list, d_type=None):
        """ Takes in a list and returns its corresponding NumPy array."""
        return np.array(lst, dtype=d_type)

    def from_tuple(self, tpl: tuple, d_type=None):
        """ Takes in a tuple and returns its corresponding NumPy array."""
        return np.array(tpl, dtype=d_type)

    def from_iterable(self, itr, d_type=None):
        """  Takes in an iterable and returns an array which contains all of its elements. """
        return np.array(itr, dtype=d_type)

    def from_shape(self, shape, value=0, d_type=None):
        """ Returns an array filled with the same value.
        The first argument is a tuple which specifies the shape of the array,
        and the second argument specifies the value of all the elements. This value must be 0 by default."""
        return np.full(shape, value, dtype=d_type)

    def random(self, shape:tuple, d_type=None):
        """ Returns an array filled with random values."""
        return np.empty(shape=shape, dtype=d_type)

    def identity(self, n, d_type=None):
        """ Returns an array representing the identity matrix of size n. """
        return np.identity(n, dtype=d_type)


if __name__ == '__main__':
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]], d_type=int))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    shape = (3, 5)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))
