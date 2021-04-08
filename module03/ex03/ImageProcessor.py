import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


class ImageProcessor:

    def __init__(self):
        pass

    def load(self, path: str):
        """ Returns an array with the RGB values of the image pixels."""

        if not isinstance(path, str):
            raise ValueError(f"Invalid argument type expected str got={type(path)}")
        im = Image.open(path)
        width, height = im.size  # get the dimensions of the image.
        pixels_array = np.array(im)  # Make a Numpy array
        print("Loading image of dimensions {} x {}".format(width, height))
        return pixels_array

    def display(self, array):
        """ Takes a NumPy array as an argument and displays the corresponding RGB image. """
        a11 = array.reshape(array.shape)
        plt.imshow(a11)
        # plt.colorbar() # This would show up a color bar on the right hand side of the image
        plt.show()


if __name__ == '__main__':
    imp = ImageProcessor()
    arr = imp.load("./image.png")
    imp.display(arr)
    # print(arr)
