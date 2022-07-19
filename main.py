import PIL.Image
from termcolor import colored
import config


def open_image(path):
    return PIL.Image.open(path)


def rotate_image(image, angle: float = 270, expand: bool = True):
    return image.rotate(angle, expand=expand)


def resize_image(image, new_width: float = 100):
    width, height = image.size
    aspect = height / width
    new_height = int(new_width * aspect)
    return image.resize((new_width, new_height))


def grey_scale(image):
    return image.convert('L')


def convert_pixel_to_char(ascii: list, pixels: list, sparse: bool = True):
    if sparse:
        return ' '.join([ascii[(pixel // ((256) // len(ascii))) - 1] for pixel in pixels])

    return ''.join([ascii[(pixel // ((256) // len(ascii))) - 1] for pixel in pixels])


def add_line_break(characters: str, characters_per_line: int = 100):
    return "\n".join(
        characters[i:(i + characters_per_line)] for i in range(0, len(characters), characters_per_line))


try:
    path = config.GENERAL['path']
    image = open_image(path)
except FileNotFoundError as e:
    print('Arquivo não encontrado. Utilizando uma imagem de exemplo')
    image = open_image('linkedin-logo.png')

if config.GENERAL['HORIZONTAL_SPACE']:
    image = grey_scale(resize_image(image, config.GENERAL['WIDTH'] // 2))
else:
    image = grey_scale(resize_image(image, config.GENERAL['WIDTH']))

pixels = image.getdata()
characters = convert_pixel_to_char(config.GENERAL['ASCII_CHARACTERS'], pixels, config.GENERAL['HORIZONTAL_SPACE'])
ascii_image = add_line_break(characters, config.GENERAL['WIDTH'])
print(colored(ascii_image, 'blue'))

with open('ascii_image.txt', 'w') as f:
    f.write(ascii_image)
