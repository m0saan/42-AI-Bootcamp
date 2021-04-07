import numpy as np
from module03.ex01.ImageProcessor import ImageProcessor


class ScrapBooker:
    """ This the class representation of ScrapBooker class. the class has a bunch of methods
    that takes a NumPy array and return a new modified one."""

    def __init__(self):
        pass

    @staticmethod
    def crop(array: type(np.array), dimensions: tuple, position=(0, 0)):
        """ Crops the image as a rectangle with the given dimensions. """
        if array.shape < dimensions:
            print("dimensions cannot be larger than the current image size.")
            return
        p1, p2 = position
        x, y = dimensions
        array = array[p1:x, p2:y]
        return array

    @staticmethod
    def thin(array: type(np.array), n: int, axis: int):
        """ deletes every n-th pixel row along the specified axis. """

        lst = []
        if not axis:
            for arr in array:
                for i in range(n - 1, len(arr), n - 1):
                    if i >= len(arr):
                        break
                    tmp = np.delete(arr, i)
                    arr = tmp
                lst.append(arr)
            return np.array(lst)
        else:
            for i in range(n - 1, array.shape[0], n - 1):
                if i >= array.shape[0]:
                    break
                array = np.delete(array, i, 0)
            return array

    @staticmethod
    def juxtapose(array, n, axis):
        """ juxtaposes n copies of the image along the specified axis (0 vertical, 1 horizontal). """
        if not axis:
            for i in range(0, n):
                array = np.concatenate((array, array), axis=axis)
            return array

        else:
            tmp = array
            for i in range(0, n):
                array = np.concatenate((array, tmp), axis=axis)
            return array

    @staticmethod
    def mosaic(array, dimensions):
        """ makes a grid with multiple copies of the array."""

        return np.array(np.tile(array, dimensions))


if __name__ == '__main__':
    # sb = ScrapBooker()
    # ip = ImageProcessor()
    # arr = ip.load("image.png")
    # arr = sb.juxtapose(arr, 2, 1)
    # ip.display(arr)
    M = np.array([
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    ])
    # print(sb.crop(array=M, dimensions=(10, 3), position=(1, 1)))
    # print(sb.thin(M, 3, 0))
    # print("-----------------------------------------")

    N = np.array([["AAAAAAAAAAAA"],
                  ["BBBBBBBBBBBB"],
                  ["CCCCCCCCCCCC"],
                  ["DDDDDDDDDDDD"],
                  ["EEEEEEEEEEEE"],
                  ["FFFFFFFFFFFF"],
                  ["GGGGGGGGGGGG"],
                  ["HHHHHHHHHHHH"],
                  ["IIIIIIIIIIII"],
                  ["JJJJJJJJJJJJ"],
                  ["KKKKKKKKKKKK"],
                  ["LLLLLLLLLLLL"]
                  ])
    # print(sb.thin(N, 4, 1))

    L = M = np.array([[1, 2]])

    if __name__ == '__main__':
        sb = ScrapBooker()
        print(sb.mosaic(L, (2, 2)))
