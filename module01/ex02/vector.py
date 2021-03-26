from operator import add, sub, mul


class Vector:
    """This is the class representation of a vector"""

    def __init__(self, p1, p2=0):
        if isinstance(p1, list):
            self.values = p1
            self.size = len(p1)
        elif isinstance(p1, int) and p2 == 0:
            self.values = [float(v) for v in range(0, p1)]
            self.size = len(self.values)
        elif isinstance(p1, int) and p2 != 0:
            self.values = [float(v) for v in range(p1, p2)]
            self.size = len(self.values)
        else:
            print("No such constructor")
            return

    def __str__(self):
        return f"(Vector {self.values})"

    def __repr__(self):
        return '{self.__class__.__name__}(vales={self.values}, size={self.size})'.format(self=self)

    def __add__(self, other):
        if isinstance(self, type(other)):
            self.values = list(map(add, self.values, other.values))
        else:
            for i, v in enumerate(self.values):
                self.values[i] = v + other
        return self

    def __radd__(self, other):
        self + other
        return self

    def __sub__(self, other):
        if isinstance(self, type(other)):
            self.values = list(map(sub, self.values, other.values))
        else:
            for i, v in enumerate(self.values):
                self.values[i] = v - other
        return self

    def __rsub__(self, other):
        self + other
        return self

    def __mul__(self, other):
        if isinstance(self, type(other)):
            self.values = list(map(mul, self.values, other.values))
        else:
            for i, v in enumerate(self.values):
                self.values[i] = v * other
        return self

    def __rmul__(self, other):
        self + other
        return self


v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = v1 * 5
print(v2)
# (Vector [0.0, 5.0, 10.0, 15.0])
