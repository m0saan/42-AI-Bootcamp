from module01.ex02.vector import Vector
import numpy as np


def get_row(A, i: int) -> list:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]


def get_column(A, j: int) -> list:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j] for A_i in A]


class Matrix:
    """ This is the class representation of a Matrix which is a two-dimensional collection of numbers."""

    def __init__(self, data):
        if isinstance(data[0], list):
            self.data = []
            column_len = len(data[0])
            for ls in data:
                if len(ls) != column_len:
                    raise ValueError("Matrix elements must be of the same length.")
                self.data.append(ls)

        elif isinstance(data, tuple):
            self.data = [[float(0) for j in range(data[1])] for i in range(data[0])]

        self.shape = (len(self.data), len(self.data[0])) if data else 0

    @staticmethod
    def dot(p1, p2: Vector) -> list:
        if p1.shape[1] != p2.get_size():
            raise ValueError(f"shapes {p1.shape} and ({p2.get_size()},) not aligned")
        ls_sum = []
        for ls in p1.data:
            total = 0
            for elem1, elem2 in zip(ls, p2.values):
                total += elem1 * elem2
            ls_sum.append(total)
        return ls_sum

    def __str__(self):
        text = ""
        for lst in self.data:
            text += str(lst)

        text += (" " + str(self.shape))
        return text

    def __repr__(self):
        return '{self.__class__.__name__}(data={self.data}, size={self.shape})'.format(self=self)

    def __add__(self, other: int):
        """ Defining the addition between a matrix and a scalar. <scalar + matrix>"""
        matrix = []
        if isinstance(other, Matrix):
            for ls1, ls2 in zip(self.data, other.data):
                tmp_ls = [itm1 + itm2 for itm1, itm2, in zip(ls1, ls2)]
                matrix.append(tmp_ls)
            return Matrix(matrix)

    def __radd__(self, other: int):
        """ Defining the addition between a matrix and a scalar. <matrix + scalar>"""
        self + other

    def __sub__(self, other):
        """ Defining the subtraction between a matrix and a scalar. <scalar - matrix>"""
        matrix = []
        if isinstance(other, Matrix):
            for ls1, ls2 in zip(self.data, other.data):
                tmp_ls = [itm1 - itm2 for itm1, itm2, in zip(ls1, ls2)]
                matrix.append(tmp_ls)
            return Matrix(matrix)

        elif isinstance(other, int):
            for ls in self.data:
                matrix.append(list(map(lambda item: item - other, ls)))
            return Matrix(matrix)

    def __rsub__(self, other: int):
        """ Defining the subtraction between a matrix and a scalar. <matrix - scalar>"""
        self - other

    def __mul__(self, other):
        """ Defining the multiplication between a matrix and a scalar. <matrix * scalar>"""
        matrix = []

        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Cannot perform multiplication")
            for ls1, ls2 in zip(self.data, other.data):
                ans = []
                for itm1, itm2 in zip(ls1, ls2):
                    ans.append(itm1*itm2)
                matrix.append(ans)
            return Matrix(matrix)

        elif isinstance(other, Vector):
            for ls in self.data:
                ans = 0
                for item1, item2 in zip(ls, other.values):
                    ans += (item1 * item2)
                matrix.append(ans)
            return Matrix(matrix)

        elif isinstance(other, list):
            for ls in self.data:
                ans = 0
                for item1, item2 in zip(ls, other):
                    ans += (item1 * item2)
                matrix.append(ans)
            return Matrix(matrix)
        elif isinstance(other, int):
            for ls in self.data:
                tmp_ls = [other * elem for elem in ls]
                matrix.append(tmp_ls)
            return Matrix(matrix)

    def __rmul__(self, other):
        """ Defining the multiplication between a matrix and a scalar. <scalar * matrix>"""
        return self * other

    def __truediv__(self, other: int):
        """ Defining the division between a matrix and a scalar. <matrix / scalar>"""
        if not isinstance(other, int):
            raise RuntimeError("Unsupported operation {Matrix / Matrix}.")
        if other == 0:
            raise ValueError("Cannot divide by zero")
        matrix = []
        for ls in self.data:
            matrix.append(list(map(lambda item: item / other, ls)))
        return Matrix(matrix)

    def __rtruediv__(self, other: int):
        """ Defining the division between a matrix and a scalar. <scalar / matrix>"""
        if not isinstance(other, int):
            raise RuntimeError("Unsupported operation {Matrix / Matrix}.")
        matrix = []
        for ls in self.data:
            matrix.append(list(map(lambda item: other / item, ls)))
        return Matrix(matrix)
