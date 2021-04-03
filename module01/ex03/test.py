

from matrix import Matrix
import numpy as np

A = Matrix([[4, 8], [3, 7]])
B = Matrix([[1, 0], [5, 2]])

C = Matrix([[2, 8], [0, 9]])
D = Matrix([[5, 6], [11, 3]])

E = Matrix([[5, 2], [3, 1]])


print(A + B)
print(C - D)
print(2 * E)

m1 = Matrix([
    [5, 1, 3],
    [1, 1, 1],
    [1, 2, 1]
])
m2 = Matrix([
    [4, 1, 2],
    [6, 3, 4],
    [2, 4, 1]
])

np1 = np.array([
    [5, 1, 3],
    [1, 1, 1],
    [1, 2, 1]]
)

np2 = np.array([
    [4, 1, 2],
    [6, 3, 4],
    [2, 4, 1]
])

print(m1-m2)
print(np1-np2)


print("\nm1 => ", repr(m1))
print("\nm2 => ", repr(m2))

print("\n---------------- Test (m1 * [1, 2, 3]) ----------------")
print(m1 * [2, 5])

print("\n---------------- Test (m1 + m2) ----------------")
print(m1 + m2)

print("\n---------------- Test (m1 + 2) ----------------")
print(m1 * 2)

print("\n---------------- Test (m1 / 2) ----------------")
print(m1 / 2)

print("\n---------------- Test (m1 * m2) ----------------")
print(m1 * m2)
