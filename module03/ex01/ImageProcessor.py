import matplotlib as matplot


class ImageProcessor:

    def __init__(self):
        pass

    def load(self, path: str):
        """ Returns an array with the RGB values of the image pixels."""

        if not isinstance(path, str):
            raise ValueError(f"Invalid argument type expected str got={type(path)}")
        return None


if __name__ == '__main__':
    imp = ImageProcessor()
    arr = imp.load("../resources/42AI.png")
