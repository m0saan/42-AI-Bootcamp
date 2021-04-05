import unittest
from vector import Vector
import numpy as np

v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector(10, 16)
v4 = Vector([2, 4, 5])
v5 = Vector([2, 11, 15])
v6 = Vector([2, 11])

v_np1 = np.array([0.0, 1.0, 2.0, 3.0])
v_np2 = np.array([10, 16])
v_np3 = np.array([2, 4, 5])
v_np4 = np.array([2, 11, 15])
v_np5 = np.array([2, 11])


class TestVectorInitialization(unittest.TestCase):
    """Testing the class vector init"""

    def test_vector_elements(self):
        self.assertEqual(v1.values, [0.0, 1.0, 2.0, 3.0], "Should be equal to [0.0, 1.0, 2.0, 3.0]")

    def test_init_vector_with_int(self):
        self.assertEqual(v2.values, [0.0, 1.0, 2.0], "Should be equal [0.0, 1.0, 2.0]")

    def test_init_vector_with_min_max(self):
        self.assertEqual(v3.values, [10.0, 11.0, 12.0, 13.0, 14.0, 15.0], "should be equal to [10.0, 11.0, 12.0, "
                                                                          "13.0, 14.0, 15.0]")


class TestVectorAddition(unittest.TestCase):
    """Testing the class vector"""

    def test_vector_elements(self):
        res = v5 + v4
        self.assertEqual(np.array(res.values), v_np3 + v_np4, f"Should be equal to {v_np3 + v_np4}")

    def test_sum_vector_and_scalar(self):
        result = v1 + 5
        self.assertEqual(np.array(result.values), v_np1 + 5, f"Should be equal {v_np1 + 5}")

    def test_adding_two_vectors(self):
        result = v5 + v6
        self.assertEqual(np.array(result.values), v_np3 + v_np4, f"should be equal to {v_np3 + v_np4}")

    def test_adding_3_vectors(self):
        result = v1 + v3 + v4
        self.assertEqual(np.array(result.values), v_np1 + v_np2 + v_np3, f"should be equal to {v_np1 + v_np2 + v_np3}")


# class TestVectorSubtraction(unittest.TestCase):
#     """Testing the class vector -> Subtraction"""
#
#     def test_sub_vector_and_scalar(self):
#         result = v1 - 2
#         self.assertEqual(result.values, [-2.0, -1.0, 0.0, 1.0], "Should be equal [-2.0, -1.0, 0.0, 1.0]")
#
#     def test_adding_two_vectors(self):
#         result = v1 - v2
#         self.assertEqual(result.values, [0.0, 0.0, 0.0], "should be equal to [0.0, 0.0, 0.0]")
#
#     def test_adding_3_vectors(self):
#         result = v3 - v1 - v2
#         self.assertEqual(result.values, [10.0, 9.0, 8.0], "should be equal to  [10.0, 9.0, 8.0]")
#

if __name__ == '__main__':
    unittest.main()
