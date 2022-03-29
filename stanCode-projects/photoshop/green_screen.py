"""
File: green_screen.py
Name: Jasmin Hsu
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(bg_img, fg_img):
    """
    :param bg_img: SimpleImage, the spaceship image
    :param fg_img: SimpleImage, green screen figure image
    :return: SimpleImage, the green screen pixels are replaced by pixels of spaceship image
    """
    bg_img.make_as_big_as(fg_img)
    for x in range(fg_img.width):
        for y in range(fg_img.height):
            pixel_bg = bg_img.get_pixel(x, y)
            pixel_fg = fg_img.get_pixel(x, y)
            bigger = max(pixel_fg.red, pixel_fg.blue)
            if pixel_fg.green > bigger * 2:
                pixel_fg.red = pixel_bg.red
                pixel_fg.blue = pixel_bg.blue
                pixel_fg.green = pixel_bg.green
    return fg_img


def main():
    """
    This function conducts green screen replacement which
    is able to photoshop a person onto spaceship background
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
