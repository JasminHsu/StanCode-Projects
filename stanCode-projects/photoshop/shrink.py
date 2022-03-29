"""
File: shrink.py
Name: Jasmin Hsu
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: SimpleImage, the image with 1/2 original width and height
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(img.width):
        for y in range(img.height):
            if x % 2 == 0 and y % 2 == 0 or x == y == 0:  # Only use even pixels
                pixel_img = img.get_pixel(x, y)
                pixel_b_img = b_img.get_pixel(x/2, y/2)
                pixel_b_img.red = pixel_img.red
                pixel_b_img.blue = pixel_img.blue
                pixel_b_img.green = pixel_img.green

    return b_img


def main():
    """
    This program will shrink the original image proportionally
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
