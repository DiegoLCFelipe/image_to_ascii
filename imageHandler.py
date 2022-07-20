from PIL import Image, ImageEnhance


class ImageHandler:
    def __init__(self, teste):
        self._path = teste
        self._image = Image.open(self._path)
        self._aspect = self._image.height / self._image.width

    @property
    def image(self):
        return self._image

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def aspect(self):
        return self._aspect

    @aspect.setter
    def aspect(self, value):
        self._aspect = value

    def resize_image(self, new_width: int = 100):
        new_height = int(new_width * self._aspect)
        self._image = self._image.resize((new_width, new_height))

    def gray_scale(self):
        self._image = self._image.convert('L')

    def contrast_scale(self):
        enhancer = ImageEnhance.Contrast(self._image)
        self._image = enhancer.enhance(2.5)



