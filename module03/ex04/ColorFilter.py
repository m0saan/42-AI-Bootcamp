from module03.ex01.ImageProcessor import ImageProcessor
import numpy as np


class ColorFilter:
    """ This is the class representation of ColorFilter class. """

    def invert(self, array) -> type(np.array):
        """
        :param array: 
        :return np.array:
        Takes a NumPy array of an image as an argument and returns an array with inverted color."""

        """ Mathematically, to invert the color of one pixel,
        we subtract the pixel's color values from the maximum, 255."""
        colors_arr = array[:, :, :3]  # we have an extra alpha channel that we don't want to modify, or the
        # transparent parts of the image won't be transparent anymore.
        # We can use numpy slice notation to modify all dimensions of the array.
        colors_arr = 255 - colors_arr
        return colors_arr

    def to_blue(self, array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a blue filter.
        """
        array[:, :, 0] = 0
        array[:, :, 1] = 0
        return array

    def to_green(self, array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a green filter.
        """
        array[:, :, 0] = 0
        array[:, :, 2] = 0
        return array

    def to_red(self, array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a red filter.
        """
        array[:, :, 1] = 0
        array[:, :, 2] = 0
        return array

    def to_red(self, array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a red filter.
        """
        array[:, :, 0] = 81
        array[:, :, 1] = 81
        array[:, :, 2] = 83
        return array


if __name__ == '__main__':
    imp = ImageProcessor()
    arr = imp.load("42AI.png")
    # print(arr)
    cf = ColorFilter()
    # arr = cf.invert(arr)
    # print(arr)

    arr = cf.to_(arr)
    imp.display(arr)
