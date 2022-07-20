from imageHandler import ImageHandler
from pixelsToASCII import PixelsToASCII
import config

path = config.GENERAL['path']
image = ImageHandler(path)
image.gray_scale()
image.contrast_scale()

if config.GENERAL['HORIZONTAL_SPACE']:
    image.resize_image(config.GENERAL['WIDTH'] // 2)
else:
    image.resize_image(config.GENERAL['WIDTH'])

image_pixels = image.image.getdata()
ascii_image = PixelsToASCII(image_pixels,
                            config.GENERAL['ASCII_CHARACTERS'],
                            config.GENERAL['WIDTH'],
                            True)

print(ascii_image)

# with open('ascii_image.txt', 'w') as f:
#     f.write(ascii_image)
