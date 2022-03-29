"""
File: caesar.py
Name: Jasmin Hsu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Use secret number to decipher the message
    """
    roll = str(input('Your guess: ')
    pic = str(input('Your g: '))
    guess = str(input('Your guess: '))




#     secret = str(input('Secret number: '))
#     cipher = str(input("What's the ciphered string? "))
#     message = decipher(cipher, secret)
#     print('The deciphered string is: '+str(message))
#
#
# def decipher(cipher, secret):
#     cipher = cipher.upper()  # Case-insensitive
#     message = ''
#     for i in range(len(cipher)):
#         ch = cipher[i]
#         num = ALPHABET.find(ch)  # Find out the number of this character in the ALPHABET
#         if num != -1:  # This character is in ALPHABET
#             num = num + int(secret)  # Shift to decipher
#             if num > 25:  # Need to wrap around
#                 num -= len(ALPHABET)
#             ch = ALPHABET[num]
#             message += ch
#         elif num == -1:  # This character is not in ALPHABET. It could be a blank or symbol
#             message += ch
#     return message

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
