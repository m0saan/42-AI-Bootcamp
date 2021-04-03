import unittest
import numpy as np
from module02.ex05.TinyStatistician import TinyStatistician

A = [1, 2, 3, 4]
B = [1, 2, 3, 4, 5]
C = [3, 5, 7, 12, 13, 14, 21, 23, 23, 23, 23, 29, 40, 56]
D = [3, 5, 12]
E = [1, 2, 3, 4]

t_stat = TinyStatistician()


class TestTinyStatistician(unittest.TestCase):

    def test_mean(self):
        """Testing the mean method."""

        self.assertEqual(t_stat.mean(A), np.array(A).mean(), f"should be equal to {np.array(A).mean()}")
        self.assertEqual(t_stat.mean(B), np.array(B).mean(), f"should be equal to {np.array(B).mean()}")
        self.assertEqual(t_stat.mean(C), np.array(C).mean(), f"should be equal to {np.array(C).mean()}")
        self.assertEqual(t_stat.mean(D), np.array(D).mean(), f"should be equal to {np.array(D).mean()}")

    def test_median(self):
        """Testing the median method."""

        self.assertEqual(t_stat.median(A), np.median(A), f"should be equal to {np.median(A)}")
        self.assertEqual(t_stat.median(B), np.median(B), f"should be equal to {np.median(B)}")
        self.assertEqual(t_stat.median(C), np.median(C), f"should be equal to {np.median(C)}")
        self.assertEqual(t_stat.median(D), np.median(D), f"should be equal to {np.median(D)}")


if __name__ == '__main__':
    unittest.main()
