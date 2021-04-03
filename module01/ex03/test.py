#  import unittest
#
#  m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
#  m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
#  m3 = Matrix((3, 3))
#
#
#  # print(m1 * m2)
#
#
#  # (Matrix [[28., 34.], [56., 68.]])
#
#  class TestVectorInitialization(unittest.TestCase):
#      """Testing the class vector init"""
#
#      def test_list_initialization1(self):
#          self.assertEqual(m1.data, [[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]], "Should be equal to [[0.0, 1.0, "
#                                                                                  "2.0, 3.0], [0.0, 2.0, 4.0, 6.0]]")
#          self.assertEqual(m1.shape, (2, 4), "should be equal (3, 2)")
#
#      def test_list_initialization2(self):
#          self.assertEqual(m2.data, [[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]], "Should be equal [[0.0, 1.0], "
#                                                                                      "[2.0, 3.0], [4.0, 5.0], [6.0, "
#                                                                                      "7.0]]")
#          self.assertEqual(m2.shape, (3, 2), "should be equal to (3, 2)")
#
#      def test_init_matrix_with_tuple(self):
#          self.assertEqual(m3.data, [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "should be equal to [[0.0, 0.0, "
#                                                                                         "0.0], [0.0, 0.0, 0.0],[0.0, "
#                                                                                         "0.0, 0.0]]")
#
#
#  if __name__ == '__main__':
#      unittest.main()


from matrix import Matrix

m1 = Matrix([
    [5, 1, 3],
    [1, 1, 1],
    [1, 2, 1]
])
m2 = Matrix([
    [5, 1, 3],
    [1, 1, 1],
    [1, 2, 1]
])
print("\nm1 => ", repr(m1))
print("\nm2 => ", repr(m2))

print("\n---------------- Test (m1 * [1, 2, 3]) ----------------")
print(m1 * [1, 2, 3])

print("\n---------------- Test (m1 + m2) ----------------")
print(m1 + m2)

print("\n---------------- Test (m1 + 2) ----------------")
print(m1 * 2)

print("\n---------------- Test (m1 / 2) ----------------")
print(m1 / 2)

print("\n---------------- Test (m1 * m2) ----------------")
print(m1 * m2)
