"""
File: boggle.py
Name: Jasmin Hsu
----------------------------------------
This program is to make a boggle game.
First settle the 4 x 4 letters into the grid and
use python to search for words that can be
constructed from the letters of sequentially adjacent
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
LENGTH = 4

# Global variable
dictionary = []


def main():
	"""
	Print out all valid words after create a 4 x 4 grid of letters
	"""
	start = time.time()
	####################
	# boggle = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	boggle = []
	for i in range(4):
		letters = input(f'{i+1} row of letters: ').lower()
		letters = letters.split()
		passage = []
		for j in range(len(letters)):
			if len(letters[j]) == 1 and letters[j].isalpha() and len(letters) == 4:
				pass
			else:
				print('Illegal input')
				passage = None
				break
		if passage is None:
			break
		else:
			boggle.append(letters)
	read_dictionary()
	search_word(boggle)

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def search_word(boggle):
	"""
	Find words that are horizontally, vertically, and diagonally neighboring
	:param boggle: (lst) The letter grid inputted by user
	"""
	word_lst = []

	for i in range(LENGTH):
		for j in range(LENGTH):
			word = ''
			coordinate = []
			word += boggle[i][j]
			coordinate.append((i, j))
			helper(boggle, word, i, j, coordinate, word_lst)
	print('There are', len(word_lst), 'words in total.')


def helper(boggle, word, x, y, coordinate, word_lst):
	if len(word) >= LENGTH:
		if word not in word_lst:
			if word in dictionary:
				print('Found:', word)
				word_lst.append(word)
				# To find words that have more than 4 letters
				longer_word_helper(boggle, word, x, y, coordinate, word_lst)

	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if (i, j) != (0, 0):
					if 0 <= x+i < 4 and 0 <= y+j < 4 and (x+i, y+j) not in coordinate:
						# Choose
						word += boggle[x+i][y+j]
						coordinate.append((x+i, y+j))
						# Explore
						if has_prefix(word) is True:
							helper(boggle, word, x+i, y+j, coordinate, word_lst)
						# Un-choose
						word = word[:-1]
						coordinate.pop()


def longer_word_helper(boggle, word, x, y, coordinate, word_lst):
	if word not in word_lst:
		if word in dictionary:
			print('Found:', word)
			word_lst.append(word)
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if (i, j) != (0, 0):
					if 0 <= x+i < 4 and 0 <= y+j < 4 and (x+i, y+j) not in coordinate:
						# Choose
						word += boggle[x+i][y+j]
						coordinate.append((x+i, y+j))
						# Explore
						if has_prefix(word) is True:
							helper(boggle, word, x+i, y+j, coordinate, word_lst)
						# Un-choose
						word = word[:-1]
						coordinate.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			dictionary.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
