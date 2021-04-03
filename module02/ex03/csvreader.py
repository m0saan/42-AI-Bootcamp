class CsvReader:

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.fp = None  # Register the opened file.
        self.header_line = ""
        self.data = []

    def __enter__(self):
        self.fp = open(self.filename, "r")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

    def print_data(self):
        for i, line in enumerate(self.data):
            if self.skip_top < i < len(self.data) - self.skip_bottom:
                print(line, end="")

    def getdata(self):
        lines = self.fp.readlines()
        n_of_elements = len(lines[1].split(self.sep))
        if self.header:
            self.header_line = lines[0]
        for line in lines:
            line = line[:len(line)-1]
            split_line = line.split(self.sep)
            if len(split_line) != n_of_elements:
                return None
            self.data.append(split_line)
        self.print_data()

    def getheader(self):
        return self.header_line


if __name__ == "__main__":
    with CsvReader('file.csv', header=True, skip_top=10, skip_bottom=10) as file:
        file.getdata()
        header = file.getheader()
