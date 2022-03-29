"""
File: complement.py
Name: Jasmin Hsu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
The program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program obtain DNA sequence and produce its complement strand
    """
    dna = str(input("Please give me a DNA strand and I'll find the complement: "))
    new_dna = build_complement(dna)
    print('The complement of '+str(dna)+' is '+str(new_dna))


def build_complement(dna):
    """
    :param dna: str, the original DNA sequence entered by the user
    :return new_dna: str, the complement strand of original DNA
    """
    new_dna = ''
    dna = dna.upper()  # Case-insensitive
    for i in range(len(dna)):
        if dna[i] == 'A':
            new_dna += 'T'
        elif dna[i] == 'T':
            new_dna += 'A'
        elif dna[i] == 'C':
            new_dna += 'G'
        elif dna[i] == 'G':
            new_dna += 'C'
    return new_dna


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
