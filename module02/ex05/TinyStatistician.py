from typing import Optional
import numpy as np


class TinyStatistician:
    """This the class representation of TinyStatistician. A class that implements mean, median, quartiles,
    variance or standard deviation """

    def __init__(self):
        pass

    def mean(self, x: list) -> Optional[float]:
        """Calculate the mean of a given list"""

        if x:
            return float(sum(x) / len(x))
        return None

    def median(self, x: list) -> Optional[float]:
        """Calculate the median of a given list"""

        if x:
            x.sort()
            if len(x) % 2 == 0:
                middle = len(x) // 2
                m1 = x[middle]
                m2 = x[middle - 1]
                return float((m1 + m2) / 2)
            else:
                return float(x[len(x) // 2])
        return None

    def quartiles(self, x: list, percentile):

        median = self.median(x)

        # find median of lower half and upper half of the list
        # find median
        print(((len(x) + 1) * (median / 100)) * percentile)


t = TinyStatistician()
A = [5, 7, 4, 4, 6, 2, 8]
print(np.quantile(A, 0.7))
t.quartiles(A, 0.7)
