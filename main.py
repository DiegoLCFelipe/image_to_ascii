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


try:
    path = config.GENERAL['path']
    image = open_image(path)
except FileNotFoundError as e:
    print('Arquivo não encontrado. Utilizando uma imagem de exemplo')
    image = open_image('linkedin-logo.png')

# try:
#
#
#     ASCII_CHARACTERS = ['.', '1', "1", "1", "#", "&", ".", "$", "$", "@", "#"]


image_rotated = resize_image(image, 50)
image_rotated_grey = grey_scale(image_rotated)
pixels = image_rotated_grey.getdata()

characters = ' '.join([config.GENERAL['ASCII_CHARACTERS'][pixel // 30] for pixel in pixels])
image_ascii = "\n".join(characters[i:(i + 100)] for i in range(0, len(characters), 100))
print(colored(image_ascii, 'blue'))

with open('ascii_image.txt', 'w') as f:
    f.write(image_ascii)
