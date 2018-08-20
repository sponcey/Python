from __future__ import print_function
import random

# From a dictionary (list) of words (strings), search through the list, and randomly pull a word of determined length (i.e. 5 characters).0

# Open text file for reading
f = open('lib/ukacd.txt', 'r')

# Store content in a variable
content = f.read()

# close the file
f.close()

# Print the length of the string
print(len(content))

# Count the number of spaces in content
def char_frequency(str1, char):
    count = 0
    for n in str1:
        if n == char:
            count += 1
    return count

print(char_frequency(content, '\n'))

# Make list from content, using character breaks to divide list, and deleting all content up to first word in content
list(content)

content_list = content.split('\n')

del content_list[0:25]

print(content_list[4])

# Print random word from list
print(random.choice(content_list))

# From a dictionary (list) of words (strings), search through the list, and randomly pull words of cascading length (str.leng()) (10, 9, 8, 7, ...)