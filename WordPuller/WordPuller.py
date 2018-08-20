from __future__ import print_function
import random

# From a dictionary (list) of words (strings), search through the list, and randomly pull a word of determined length (i.e. 5 characters).0

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

# if random word is a certain length, print it. if it isn't that length, keep looking until you find a random word of that length, then stop.
#!! current problem: how do I redefine the random_word variable when the word isn't the desired length?

def wordlength(length):
    # defining variable for random word
    random_word = random.choice(content_list)
    
    if len(random_word) == length:
        break
    print(random_word)
    elif len(random_word) != length:
        continue
        
print(wordlength(5))
    
# From a dictionary (list) of words (strings), search through the list, and randomly pull words of cascading length (str.leng()) (10, 9, 8, 7, ...)