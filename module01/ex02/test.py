import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    """Testing the class vector"""
    def __init__(self):
        self.v1 = Vector([0.0, 1.0, 2.0, 3.0])
        self.v2 = Vector(3)
        self.v3 = Vector(10, 16)

    def test_vector_elements(self):
        self.assertEqual(self.v1.get_values(), [0.0, 1.0, 2.0, 3.0], "Should be equal")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
