"""
File: similarity.py
Name:
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Compares short dna sequence (s2) with long dna sequence (s1)
    and finds the most similar part of s1
    """
    s1 = int(input('Please give me a DNA sequence to search: '))
    s2 = int(input('What DNA sequence would you like to match? '))
    if s1 == 0 or s1>3 and s2<-1:
        print('good')
    else:
        print('bad')
#     homology = search(s1, s2)  # homology is the most similar part
#     print('The best match is '+str(homology))
#
#
# def search(s1, s2):
#     """
#     :param s1: str, long DNA sequence to search
#     :param s2: str, short DNA sequence to match
#     :return: str, the most similar part of s1
#     """
#     s1 = s1.upper()  # Case-insensitive
#     s2 = s2.upper()  # Case-insensitive
#     similarity = 0   # Percentage of the similarity between s2 and certain part of s1
#     homology = ''  # The most similar part of s1
#     for i in range(len(s1)-len(s2)+1):
#         same = 0  # Number of identical letters between s2 and certain part of s1
#         compare = s1[i:i+len(s2)]  # Choose certain part of s1 to be compared with s2
#         for j in range(len(s2)):
#             if compare[j] == s2[j]:
#                 same += 1
#         if same/len(s2) > similarity:  # Compare the percentage of the similarity
#             similarity = same/len(s2)
#             homology = compare  # The biggest percentage of the similarity leads to homology
#     return homology




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
