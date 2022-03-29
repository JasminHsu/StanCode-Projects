"""
File: mirror_lake.py
Name: Jasmin Hsu
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: A new mirror symmetry image and the height is twice as high as the original one
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height * 2)  # Create a blank image
    for x in range(img.width):
        for y in range(img.height):
            # Build upper part of blank image
            pixel_img = img.get_pixel(x, y)
            pixel_b_img = b_img.get_pixel(x, y)
            pixel_b_img.red = pixel_img.red
            pixel_b_img.blue = pixel_img.blue
            pixel_b_img.green = pixel_img.green

            # Build lower part of blank image
            pixel_img = img.get_pixel(x, y)
            pixel_b_img = b_img.get_pixel(x, b_img.height - 1 - y)
            pixel_b_img.red = pixel_img.red
            pixel_b_img.blue = pixel_img.blue
            pixel_b_img.green = pixel_img.green
    return b_img


def main():
    """
    This program will use reflect() function to output a new
    image that contains mirror symmetry view
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
