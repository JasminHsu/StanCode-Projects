"""
File: blur.py
Name: Jasmin Hsu
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blurred image with new RBG value of every pixel
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)

            # This point is the upper left corner, surrounded by 3 points
            if x == y == 0:
                img_pixel_1 = img.get_pixel(x, y + 1)
                img_pixel_2 = img.get_pixel(x + 1, y)
                img_pixel_3 = img.get_pixel(x + 1, y + 1)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red) // 4
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue) // 4
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green) // 4

            # This point is the lower right corner, surrounded by 3 points
            elif x + y == img.height + img.width - 2:
                img_pixel_1 = img.get_pixel(x, y - 1)
                img_pixel_2 = img.get_pixel(x - 1, y)
                img_pixel_3 = img.get_pixel(x - 1, y - 1)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red) // 4
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue) // 4
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green) // 4

            # This point is the upper right corner, surrounded by 3 points
            elif x == img.width - 1 and y == 0:
                img_pixel_1 = img.get_pixel(x, y + 1)
                img_pixel_2 = img.get_pixel(x - 1, y)
                img_pixel_3 = img.get_pixel(x - 1, y + 1)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red) // 4
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue) // 4
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green) // 4

            # This point is the lower left corner, surrounded by 3 points
            elif x == 0 and y == img.height - 1:
                img_pixel_1 = img.get_pixel(x, y - 1)
                img_pixel_2 = img.get_pixel(x + 1, y)
                img_pixel_3 = img.get_pixel(x + 1, y - 1)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red) // 4
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue) // 4
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green) // 4

            # These points are in the first row, and each point is surrounded by 5 points
            elif y == 0:
                img_pixel_1 = img.get_pixel(x - 1, y)
                img_pixel_2 = img.get_pixel(x - 1, y + 1)
                img_pixel_3 = img.get_pixel(x, y + 1)
                img_pixel_4 = img.get_pixel(x + 1, y + 1)
                img_pixel_5 = img.get_pixel(x + 1, y)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red + img_pixel_5.red) // 6
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue + img_pixel_5.blue) // 6
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green + img_pixel_5.green) // 6

            # These points are in the last row, and each point is surrounded by 5 points
            elif y == img.height - 1:
                img_pixel_1 = img.get_pixel(x - 1, y)
                img_pixel_2 = img.get_pixel(x - 1, y - 1)
                img_pixel_3 = img.get_pixel(x, y - 1)
                img_pixel_4 = img.get_pixel(x + 1, y - 1)
                img_pixel_5 = img.get_pixel(x + 1, y)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red + img_pixel_5.red) // 6
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue + img_pixel_5.blue) // 6
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green + img_pixel_5.green) // 6

            # These points are in the first column, and each point is surrounded by 5 points
            elif x == 0:
                img_pixel_1 = img.get_pixel(x, y - 1)
                img_pixel_2 = img.get_pixel(x + 1, y - 1)
                img_pixel_3 = img.get_pixel(x + 1, y)
                img_pixel_4 = img.get_pixel(x + 1, y + 1)
                img_pixel_5 = img.get_pixel(x, y + 1)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red + img_pixel_5.red) // 6
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue + img_pixel_5.blue) // 6
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green + img_pixel_5.green) // 6

            # These points are in the last column, and each point is surrounded by 5 points
            elif x == img.width - 1:
                img_pixel_1 = img.get_pixel(x, y - 1)
                img_pixel_2 = img.get_pixel(x - 1, y - 1)
                img_pixel_3 = img.get_pixel(x - 1, y)
                img_pixel_4 = img.get_pixel(x - 1, y + 1)
                img_pixel_5 = img.get_pixel(x, y + 1)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red + img_pixel_5.red) // 6
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue + img_pixel_5.blue) // 6
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green + img_pixel_5.green) // 6

            # These points are surrounded by 8 points
            else:
                img_pixel_1 = img.get_pixel(x - 1, y)
                img_pixel_2 = img.get_pixel(x + 1, y)
                img_pixel_3 = img.get_pixel(x - 1, y - 1)
                img_pixel_4 = img.get_pixel(x, y - 1)
                img_pixel_5 = img.get_pixel(x + 1, y - 1)
                img_pixel_6 = img.get_pixel(x - 1, y + 1)
                img_pixel_7 = img.get_pixel(x, y + 1)
                img_pixel_8 = img.get_pixel(x + 1, y + 1)
                new_r = (img_pixel.red + img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red + img_pixel_5.red + img_pixel_6.red + img_pixel_7.red + img_pixel_8.red) // 9
                new_b = (img_pixel.blue + img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue + img_pixel_5.blue + img_pixel_6.blue + img_pixel_7.blue + img_pixel_8.blue) // 9
                new_g = (img_pixel.green + img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green + img_pixel_5.green + img_pixel_6.green + img_pixel_7.green + img_pixel_8.green) // 9
            new_img_pixel = new_img.get_pixel(x, y)
            new_img_pixel.red = new_r
            new_img_pixel.blue = new_b
            new_img_pixel.green = new_g
    return new_img


def main():
    """
    This program will use blur() function to make original
    image become blurred by changing the RBG value of every pixel
    into average RBG value of adjacent points
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
