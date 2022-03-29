"""
File: sierpinski.py
Name: Jasmin Hsu
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine, GPolygon
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow


# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Draw Sierpinski Triangle by recursion
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: control the order of triangle
	:param length: the length of the 1st triangle
	:param upper_left_x: the x coordinate of the 1st triangle
	:param upper_left_y: the y coordinate of the 1st triangle
	"""
	if order == 0:
		pass
	else:
		# Draw triangle
		tri_line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		tri_line2 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.866)
		tri_line3 = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.866)

		window.add(tri_line1)
		window.add(tri_line2)
		window.add(tri_line3)
		pause(10)

		# Upper left
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# Upper right
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		# Lower one
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length * 0.866 / 2)


if __name__ == '__main__':
	main()