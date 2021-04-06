from module03.ex01.ImageProcessor import ImageProcessor
import numpy as np


class ColorFilter:
    """ This is the class representation of ColorFilter class. """

    def invert(self, array) -> type(np.array):
        """
        :param array: 
        :return np.array:
        Takes a NumPy array of an image as an argument and returns an array with inverted color."""

        lst = []
        for i in range(0, array.shape[0]):
            tmp_list = []
            for j in range(0, array.shape[1]):
                tmp_list.append(array[i][j])
            lst.append(tmp_list)
        return np.array(lst)

    def to_blue(self, array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a blue filter.
        """
        pass


if __name__ == '__main__':
    imp = ImageProcessor()
    arr = imp.load("42AI.png")
    print(arr)
    cf = ColorFilter()
    cf.invert(arr)
    print(arr)
    imp.display(arr)
