"""
File: anagram.py
Name: Jasmin Hsu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
python_list = []


# Ask user to input a word and decide if the word should enter recursion
def main():
    start = time.time()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        target = input('Find anagrams for: ').lower()
        if target == EXIT:
            break
        else:
            read_dictionary()
            find_anagrams(target)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


# Create a list to store all words in the dictionary
def read_dictionary():
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()
            python_list.append(word)


def find_anagrams(s):
    """
    :param s: The word input by user
    """
    all_anagrams = []
    helper(s, '', all_anagrams)
    print(f'{len(all_anagrams)} anagrams: {all_anagrams}')


def helper(target, current_lst, all_anagrams):
    if len(current_lst) == len(target):
        if current_lst in python_list:
            all_anagrams.append(current_lst)
            print('Searching...')
            print(f'Found: {current_lst}')

    else:
        for i in range(len(target)):
            if target[i] in current_lst:
                pass
            else:
                # Choose
                current_lst += target[i]
                # Explore
                if has_prefix(target) is True:
                    helper(target, current_lst, all_anagrams)
                # Un-choose
                current_lst = current_lst[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: str
    :return: bool
    """
    for word in python_list:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
