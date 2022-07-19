import PIL.Image
from termcolor import colored
import config

N_CHAR_BEFORE_LINE_BREAK = 100


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


def convert_pixel_to_char(ascii: list, pixels: list):
    return ' '.join([ascii[pixel // (N_CHAR_BEFORE_LINE_BREAK//2)] for pixel in pixels])


try:
    path = config.GENERAL['path']
    image = open_image(path)
except FileNotFoundError as e:
    print('Arquivo não encontrado. Utilizando uma imagem de exemplo')
    image = open_image('linkedin-logo.png')


image_rotated = resize_image(image, N_CHAR_BEFORE_LINE_BREAK//2)
image_rotated_grey = grey_scale(image_rotated)
pixels = image_rotated_grey.getdata()

characters = convert_pixel_to_char(config.GENERAL['ASCII_CHARACTERS'], pixels)

image_ascii = "\n".join(characters[i:(i + 100)] for i in range(0, len(characters), 100))
print(colored(image_ascii, 'blue'))

with open('ascii_image.txt', 'w') as f:
    f.write(image_ascii)
