"""
File: fire.py
Name: Jasmin Hsu
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting red pixel
HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image
    :return: The image that fires are highlighted
    """
    img = SimpleImage(filename)
    for x in range(img.width):
        for y in range(img.height):
            pixel_img = img.get_pixel(x, y)
            avg = (pixel_img.blue + pixel_img.red + pixel_img.green) // 3
            if pixel_img.red > avg * HURDLE_FACTOR:  # Detect the fire areas
                pixel_img.red = 255
                pixel_img.green = 0
                pixel_img.blue = 0
            else:  # Areas without fire turn into grey
                pixel_img.red = avg
                pixel_img.green = avg
                pixel_img.blue = avg
    return img


def main():
    """
    This program will use highlight_fire() function to find out
    the fire areas and make remaining areas turn into grey to
    highlight those fires
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
