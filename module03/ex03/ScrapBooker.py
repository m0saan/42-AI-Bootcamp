import numpy as np


class ScrapBooker:
    """ This the class representation of ScrapBooker class. the class has a bunch of methods
    that takes a NumPy array and return a new modified one."""

    def __init__(self):
        pass

    def crop(self, array: type(np.array), dimensions: tuple, position=(0, 0)):
        """ Crops the image as a rectangle with the given dimensions. """
        if array.shape < dimensions:
            print("dimensions cannot be larger than the current image size.")
            return
        p1, p2 = position
        x, y = dimensions
        array = array[p1:x, p2:y]
        return array

    def thin(self, array: type(np.array), n: int, axis: int):
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
            for i in range(n - 1, array.shape[0], n-1):
                if i >= array.shape[0]:
                    break
                array = np.delete(array, i, 0)
            return array

    def juxtapose(self, array, n, axis):
        """ juxtaposes n copies of the image along the specified axis (0 vertical, 1 horizontal). """

if __name__ == '__main__':
    sb = ScrapBooker()
    M = np.array([
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    ])
    # print(sb.crop(array=M, dimensions=(10, 3), position=(1, 1)))
    print(sb.thin(M, 3, 0))
    print("-----------------------------------------")

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
    print(sb.thin(N, 4, 1))
