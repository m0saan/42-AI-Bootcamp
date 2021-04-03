from module01.ex02.vector import Vector

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
        for ls in self.data:
            matrix.append(list(map(lambda item: item + other, ls)))
        return Matrix(matrix)

    def __radd__(self, other: int):
        """ Defining the addition between a matrix and a scalar. <matrix + scalar>"""
        self + other

    def __sub__(self, other: int):
        """ Defining the subtraction between a matrix and a scalar. <scalar - matrix>"""
        matrix = []
        if isinstance(other, Vector):
            return self.dot(self, other)

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
            if self.shape[1] != other.shape[0]:
                raise ValueError("Cannot perform multiplication")
            ans = [[0 for x in range(other.shape[1])] for y in range(self.shape[0])]
            n_columns = 0
            for i, ls in enumerate(self.data):
                _sum = 0
                for j, v in enumerate(ls):
                    for k, l in enumerate(get_column(other.data, n_columns)):
                        _sum += (self.data[i][k] + other.data[k][j])
                    ans[i][j] = _sum
            return Matrix(ans)

        for ls in self.data:
            matrix.append(list(map(lambda item: item * other, ls)))
        return Matrix(matrix)

    def __rmul__(self, other):
        """ Defining the multiplication between a matrix and a scalar. <scalar * matrix>"""
        self * other

    def __truediv__(self, other: int):
        """ Defining the multiplication between a matrix and a scalar. <matrix / scalar>"""
        if other == 0:
            raise ValueError("Cannot divide by zero")
        matrix = []
        for ls in self.data:
            matrix.append(list(map(lambda item: item / other, ls)))
        return Matrix(matrix)

    def __rtruediv__(self, other: int):
        """ Defining the multiplication between a matrix and a scalar. <scalar / matrix>"""
        self / other


m1 = Matrix([[4, 1], [6, 3], [2, 4]])
m2 = Matrix([[2, 5, 2, -5], [3, 5, -2, 4]])



v_sum = m1 * 5

print(v_sum)

# m2 = m1 + 2
# m3 = m1 * 2
# m4 = m1 / 2
# print(m2)
# print(m3)
# print(m4)
# (Matrix [[28., 34.], [56., 68.]])
