"""
File: rocket.py
Name: Jasmin Hsu
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This rocket consists of six parts
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	If the rocket head has n row (=SIZE), the first row will
	have n blanks plus 1 "/" plus 1 "\" plus n blanks; and
	the second row will have (n-1) blanks plus (1+1) "/" plus
	(1+1) "\" plus (n-1) blanks, etc.
	"""
	n = SIZE
	for i in range(SIZE):
		for j in range(n):
			print(' ', end="")
		for k in range(i+1):
			print('/', end="")
		for k in range(i+1):
			print('\\', end="")
		for j in range(n):
			print(' ', end="")
		n -= 1
		print('')


def belt():
	"""
	The first symbol and the last symbol are "+" and there
	are (SIZE*2) "=" in the middle
	"""
	print('+', end="")
	for i in range(SIZE*2):
		print('=', end="")
	print('+')


def upper():
	"""
	The first symbol and the last symbol of each row is "|".
	In the middle of first row has (SIZE-1) "." plus 1 "/\"
	plus (SIZE-1)"."; second row has (SIZE-2) "." plus (1+1)
	"/\" plus (SIZE-2) ".", etc.
	"""
	n = SIZE
	for i in range(SIZE):
		print('|', end="")
		for j in range(n-1):
			print('.', end="")
		for k in range(i+1):
			print('/', end="")
			print('\\', end="")
		for j in range(n-1):
			print('.', end="")
		print('|')
		n -= 1


def lower():
	"""
	The first symbol and the last symbol of each row is "|".
	In the middle of first row has 0 "." plus SIZE "/\" plus
	0 "."; second row has (0+1) "." plus (SIZE-1) "/\" plus
	(0+1) ".", etc.
	"""
	n = SIZE
	for i in range(SIZE):
		print('|', end="")
		for j in range(i):
			print('.', end="")
		for k in range(n):
			print('\\', end="")
			print('/', end="")
		for j in range(i):
			print('.', end="")
		print('|')
		n -= 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()