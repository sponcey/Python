from __future__ import print_function
import random

# GOAL: From a dictionary (list) of words (strings), search through the list, and randomly pull a word of determined length (i.e. 5 characters).

## BUGS: When user inputs character value that is higher than any word in dictionary, program crashes/won't stop looking.

# Open text file for reading
f = open('lib/ukacd.txt', 'r')
content = f.read()
f.close()

# Make list from content, using character breaks to divide list, and deleting all content up to first word in content
list(content)
content_list = content.split('\n')
del content_list[0:25]

content_list_caps = []
for word in content_list:
    content_list_caps.append(word.upper())

# wordlength function defines a list made up of words of a specified length.
def wordlength(length):
    # first, define a list that fulfills the desired attribute of length
    outputwords = []
    # for every word in the list, if the word matches the length, append it to the list
    for w in content_list_caps:
        if len(w) == length:
            outputwords.append(w)
    # if there are no words in the list, let me know!
    if len(outputwords) == 0:
        print("Can't find any words that length!")
    # otherwise, randomly select a word from the new list
    else:
        print(random.choice(outputwords))          

# Now that the word length function is defined, nest that function in another function that iterates across a range of word lengths.
def wordlength_range(hichar, lowchar):
    while True:
        wordlength(hichar)
        if hichar != lowchar:
            hichar = hichar-1
        if hichar == lowchar:
            break
            
wordlength_range(100,3)
    
# Mission Accomplished!!