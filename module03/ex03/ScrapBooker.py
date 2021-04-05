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
                tmp = []
                for i in range(0, len(arr), n):
                    if i <= len(arr):
                        tmp = np.delete(arr, i+n)
                        arr = tmp
                lst.append(arr)
            return np.array(lst)
        else:
            print("YAy.")


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

