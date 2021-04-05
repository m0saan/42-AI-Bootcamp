from operator import add, sub, mul


class Vector:
    """This is the class representation of a vector"""

    def __init__(self, p1, p2=0):
        if isinstance(p1, list):
            self.__values = p1
            self.__size = len(p1)
        elif isinstance(p1, int) and p2 == 0:
            self.__values = [float(v) for v in range(0, p1)]
            self.__size = len(self.__values)
        elif isinstance(p1, int) and p2 != 0:
            self.__values = [float(v) for v in range(p1, p2)]
            self.__size = len(self.__values)
        else:
            print("No such constructor")
            return

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, v):
        if not v:
            raise ValueError("List cannot be empty.")

    def get_size(self):
        return self.__size

    def __str__(self):
        return f"(Vector {self.__values})"

    def __repr__(self):
        return '{self.__class__.__name__}(vales={self.values}, size={self.size})'.format(self=self)

    def __add__(self, other):

        values = []
        if isinstance(self, type(other)):
            if len(self.__values) != len(other.__values):
                raise ValueError("ValueError: operands could not be broadcast together"
                                 "with shapes ({},) ({},)".format(self.__size, other.__size))
            values = list(map(add, self.__values, other.__values))
        else:
            for i, v in enumerate(self.__values):
                values.append(v + other)
        return Vector(values)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        values = []
        if isinstance(self, type(other)):
            if len(self.__values) != len(other.__values):
                raise ValueError("ValueError: operands could not be broadcast together"
                                 "with shapes ({},) ({},)".format(self.__size, other.__size))
            values = list(map(sub, self.__values, other.__values))
        else:
            for i, v in enumerate(self.__values):
                values.append(v - other)
        return Vector(values)

    def __rsub__(self, other):
        values = []
        if isinstance(self, type(other)):
            return self - other
        else:
            for i, v in enumerate(self.__values):
                values.append(other - v)
        return Vector(values)

    def __mul__(self, other):
        values = []
        if isinstance(self, type(other)):
            if len(self.__values) != len(other.__values):
                raise ValueError("ValueError: operands could not be broadcast together"
                                 "with shapes ({},) ({},)".format(self.__size, other.__size))
            s = 0
            for value1, value2 in zip(self.__values, other.values):
                s += (value1 * value2)
                return s
        else:
            for i, v in enumerate(self.__values):
                values.append(v * other)
        return Vector(values)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        values = []
        if isinstance(self, type(other)):
            if len(self.__values) != len(other.__values):
                raise ValueError("ValueError: operands could not be broadcast together"
                                 "with shapes ({},) ({},)".format(self.__size, other.__size))
            for value1, value2 in zip(self.__values, other.values):
                if value2 == 0:
                    raise RuntimeWarning("divide by zero encountered in true_divide")
                values.append((value1 / value2))
            return Vector(values)
        else:
            if other == 0:
                raise ZeroDivisionError("divide by zero encountered in true_divide")
            for i, v in enumerate(self.__values):
                values.append(v / other)
        return Vector(values)

    def __rtruediv__(self, other):
        values = []
        if other == 0:
            raise ZeroDivisionError("divide by zero encountered in true_divide")
        for i, v in enumerate(self.__values):
            if v == 0:
                raise RuntimeWarning("divide by zero encountered in true_divide")
            values.append(other / v)
        return Vector(values)
