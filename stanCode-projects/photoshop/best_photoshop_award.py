"""
File: best_photoshop_award.py
Name: Jasmin Hsu
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.3

# Controls the upper bound for black pixel
BLACK_PIXEL = 90


def main():
    """
    The new season of F1 has begun recently, I hope I
    will be able to watch the race in person this year.
    So this program makes a photo of me with racing cars
    """
    me_img = SimpleImage('image_contest/me.png')
    bg_img = SimpleImage('image_contest/racing.jpeg')
    combined_img = combined(me_img, bg_img)
    combined_img.show()


def combined(me_img, bg_img):
    """
    : param1 me: SimpleImage, my picture with green screen
    : param2 bg: SimpleImage, the background image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    bg_img.make_as_big_as(me_img)
    for x in range(me_img.width):
        for y in range(me_img.height):
            pixel_me = me_img.get_pixel(x, y)
            avg = (pixel_me.red + pixel_me.blue + pixel_me.green) // 3
            ttl = pixel_me.red + pixel_me.blue + pixel_me.green
            # Replace green pixels with pixels from background
            if pixel_me.green > avg * THRESHOLD and ttl > BLACK_PIXEL:
                pixel_bg = bg_img.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me_img


if __name__ == '__main__':
    main()
