from module01.ex02 import vector

class Matrix:
    """ This is the class representation of a Matrix which is a two-dimensional collection of numbers."""

    def __init__(self, *data):
        if isinstance(data[0], list):
            self.data = [ls for ls in data]

        elif isinstance(data[0], tuple):
            self.data = [[float(0) for j in range(data[0][1])] for i in range(data[0][0])]

        self.shape = (len(self.data), len(data[0])) if data else 0

    def __str__(self):
        text = ""
        for lst in self.data:
            text += str(lst)
        return text

    def __repr__(self):
        return '{self.__class__.__name__}(data={self.data}, size={self.shape})'.format(self=self)

    def __mul__(self, other: vector):
        """ Defining the multiplication between a matrix and a  vector."""
        # data = [zip(other.)]


m = Matrix((3, 3))
print(repr(m))
