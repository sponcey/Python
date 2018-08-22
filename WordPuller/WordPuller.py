from __future__ import print_function
import random

# GOAL: From a dictionary (list) of words (strings), search through the list, and randomly pull a word of determined length (i.e. 5 characters).

## BUGS: When user inputs character value that is higher than any word in dictionary, program crashes/won't stop looking.

# Open text file for reading
f = open('lib/ukacd.txt', 'r')

# Store content in a variable
content = f.read()

# close the file
f.close()

# # Count the number of spaces in content
# def char_frequency(str1, char):
#     count = 0
#     for n in str1:
#         if n == char:
#             count += 1
#     return count

# print(char_frequency(content, '\n'))

# Make list from content, using character breaks to divide list, and deleting all content up to first word in content
list(content)

content_list = content.split('\n')

del content_list[0:25]

# convert each string in the list to an integer representing the length of that string
# def converttolength(listy):
#     for n in listy[:]:
#         len(n) = n
        
# content_list_length = converttolength(content_list)

# if random word is a certain length, print it. if it isn't that length, keep looking until you find a random word of that length, then stop.
## Problem: If user gives a length of a word that can't be found in the dictionary, Python will never be able to stop!!

def wordlength(length):
    # #first check if length is even in dictionary!
    # ## how do I write this to stop looping once it's read every string?
    # while True: 
    #     for n in content_list[:]:
    #         if len(n) != length:
    #             return
    #         elif len(n) == length:
    #             continue
    #         elif len(n) != length:
    #             print("Couldn't find anything")
    #             break
    while True:
        # defining variable for random word
        random_word = random.choice(content_list)
        ## this is pretty much exactly the same as above! lol
        # for n in content_list:
        #     pickedword = len(n)
        #     if length != pickedword:
        #         return
        #     if length == pickedword:
        #         print("List contains word of this lenghth!")
        #         continue
        # since we have established there is a word of that legnth, print one of them!
        if len(random_word) == length:
            print(random_word)
            break 

wordlength(5)

# Now that the word length function is defined, nest that function in another function that iterates across a range of word lengths.

# def wordlength_range(hichar, lowchar):
#     while True:
#         wordlength(hichar)
#         if hichar != lowchar:
#             hichar = hichar-1
#         if hichar == lowchar:
#             break
            
# wordlength_range(15,3)
    
# Mission Accomplished!!