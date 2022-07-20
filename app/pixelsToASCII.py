class PixelsToASCII:
    def __init__(self, pixels, ascii_list, n_char_per_line: int, sparse: bool = True):
        self.pixels = pixels
        self.ascii_list = ascii_list
        self.n_char_per_line = n_char_per_line
        self.sparse = sparse
        self._string = None

        self.convert_pixels_to_string()
        self.add_line_breaks()

    def __str__(self):
        return 'Imagem convertida paras ASCII: \n' + self._string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value

    def convert_pixels_to_string(self):
        if self.sparse:
            self._string = ' '.join([self.ascii_list[(pixel // (256 // len(self.ascii_list))) - 1]
                                     for pixel in self.pixels])
        else:
            self._string = ''.join([self.ascii_list[(pixel // (256 // len(self.ascii_list))) - 1]
                                    for pixel in self.pixels])

    def add_line_breaks(self):
        self._string = "\n".join(self.string[i:(i + self.n_char_per_line)]
                                 for i in range(0, len(self.string), self.n_char_per_line))