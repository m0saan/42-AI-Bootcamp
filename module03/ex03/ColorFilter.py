# from module03.ex01.ImageProcessor import ImageProcessor
from ImageProcessor import ImageProcessor
import numpy as np


class ColorFilter:
    """ This is the class representation of ColorFilter class. """

    def __init__(self):
        pass

    @staticmethod
    def invert(array):
        """
        :param array:
        :return np.array:
        Takes a NumPy array of an image as an argument and returns an array with inverted color."""

        """ Mathematically, to invert the color of one pixel,
        we subtract the pixel's color values from the maximum, 255."""
        # colors_arr = array[:, :, :3]  # we have an extra alpha channel that we don't want to modify, or the
        # transparent parts of the image won't be transparent anymore.
        # We can use numpy slice notation to modify all dimensions of the array.
        return 255 - array[:, :, :3]

    @staticmethod
    def to_blue(array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a blue filter.
        """
        array[:, :, 0] = 0
        array[:, :, 1] = 0
        return array

    @staticmethod
    def to_green(array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a green filter.
        """
        array[:, :, 0] *= 0
        array[:, :, 2] *= 0
        return array

    @staticmethod
    def to_red(array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a red filter.
        """
        array[:, :, 1] = 0
        array[:, :, 2] = 0
        return array

    @staticmethod
    def to_celluloid(array):
        """
        :return: np.array
        Takes a NumPy array of an image as an argument and returns an array with a red filter.
        """

        # img[img[:, :, 0] < 255, 0] = 255
        array[array < 64] = 0
        array[(array > 64) & (array < 128)] = 64
        array[array > 128] = 128

        return array

    @staticmethod
    def to_grayscale(array, _filter):
        """Takes a NumPy array of an image as an argument and returns an array in grayscale."""

        if _filter == "m" or _filter == "mean":
            array[:, :, 0:3] = np.sum(array[:, :, 0:3] / 3, axis=2, keepdims=True).astype(array.dtype)
            return array
        elif _filter == "weighted" or _filter == "w":
            # 0.299 * R_channel + 0.587 * G_channel + 0.114 * B_channel.
            array[:, :, 0:3] = np.sum([array[:, :, 0:1] * 0.299, 0.587 * array[:, :, 1:2], 0.114 * array[:, :, 2:3]],
                                      axis=0)
            return array


if __name__ == '__main__':
    imp = ImageProcessor()
    arr = imp.load("Elon.png")
    cf = ColorFilter()

    arr = cf.to_grayscale(arr, "w")
    imp.display(arr)
