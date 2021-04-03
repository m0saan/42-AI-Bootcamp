from typing import Optional
import numpy as np


class TinyStatistician:
    """This the class representation of TinyStatistician. A class that implements mean, median, quartiles,
    variance or standard deviation """

    def __init__(self):
        pass

    def mean(self, x: list) -> Optional[float]:
        """ Calculate the mean of a given list."""

        if x:
            return float(sum(x) / len(x))
        return None

    def _median_odd(self, x: list) -> float:
        x.sort()
        return float(x[len(x) // 2])

    def _median_even(self, x: list) -> float:
        x.sort()
        middle = len(x) // 2
        m1 = x[middle]
        m2 = x[middle - 1]
        return float((m1 + m2) / 2)

    def median(self, x: list) -> Optional[float]:
        """ Calculate the median of a given list
            - If len(x) is odd, the median is the middle element.
            - If len(xs) is even, it's the average of the middle two elements.
        """
        if not x:
            return None
        return self._median_even(x) if len(x) % 2 == 0 else self._median_odd(x)

    def quartiles(self, x: list, percentile):
        """Returns the pth-percentile value in x"""
        percentile /= 100
        x.sort()
        index = int(percentile * len(x))
        return float(x[index])


t = TinyStatistician()
A = [5, 7, 4, 4, 6, 2, 8]
B = [5, 7, 4, 4, 6]

a = [1, 42, 300, 10, 59]

print(np.quantile(a, 0.70))
print(t.quartiles(a, 70))
print(t.quartiles_ab(a, 70))

# print(np.quantile(A, .50))
# print(t.quartiles(A, .50))
#
# print(np.quantile(B, .50))
# print(t.quartiles(B, .50))
#
# print(np.quantile(A, .90))
# print(t.quartiles(A, .90))
# '# t.quartiles(A, 0.7)
#
#
# 0 0 0 0 0
#
# 80
#
