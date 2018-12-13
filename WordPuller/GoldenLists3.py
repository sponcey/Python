##### GOLDEN LISTS v.1 ########################################################

## ABOUT GOLDEN LISTS:
##     This is the first version of Golden Lists! Golden Lists takes a desired word width, a tolerance,
##     word case, and a number words, and spits out words that are all exactly the same width, based on
##     whatever current font you have open!

## TO DO FOR FUTURE VERSIONS: 
##    – Build for more language support. English support only at the moment.
##    – Make a cool GUI so it's easier to input information.
##    – Word widths that take kerning into account.

## KNOWN BUGS:
##    – If there are no words in the dictionary that match desired width, script won't stop running :\

## CREDITS:
##    Thanks to Nina Stoessinger for word-o-mat. This script builds off of some of the code
##    from that wonderful script.

import random, json, os, time
from pathlib import Path

f = CurrentFont()

##### ENGLISH DICTIONARIES #################################################

# Read external text file and make it a list.
text = open('lib/ukacd.txt', 'r', encoding='latin1')
content = text.read()
text.close()
list(content)

content_list = content.split('\n')
del content_list[0:25]

content_list_caps = []
for word in content_list:
    content_list_caps.append(word.capitalize())

content_list_sc = []
for word in content_list:
    content_list_sc.append(word.upper())
    
##### USER INPUT AREA ######################################################

wordwidth = 3000              # how wide you want the word to be in units
tolerance = 50                # tolerance of how much wider or narrower word can be
usercase = content_list_sc    # choose from lists in English dictionaries (more languages to come!)
numofwords = 5                # number of words to spit out

##### DEFINING FUNCTIONS AREA ##############################################

## Function that randomly shuffles list.

def randomly(seq):
    shuffled = list(seq)
    random.shuffle(shuffled)
    return shuffled

## Function that defines list of characters in font

def fontCharacters(font):
    if not font:
        return []
    charset = []
    gnames = []
    for g in font:
        if g.unicode is not None:
            try:
                charset.append(chr(int(g.unicode)))
                gnames.append(g.name)
            except ValueError:
                pass
    return charset, gnames

## Function that takes wordlist, units, number of prints, and gives back what you want!

def sortWordsByWidth(wordlist, units, prints):
    if f is not None:
        fontChars, glyphNames = fontCharacters(f)
        glyphNamesForValues = {fontChars[i]: glyphNames[i] for i in range(len(fontChars))}
    else:
        fontChars = []
        glyphNames = []
    
    # This for loop is eating up SO MUCH PROCESSING TIME. Is there a simpler way to write this to get a quicker result? Do I really need
    # it to measure EVERY SINGLE word in the dictionary?   
    for word in wordlist:
        if prints == 0 or len(wordlist) == 0:
            break
        # elif printcounter == 0 and len(wordlist) == 0:
        #     print ("Couldn't find anything!")
        #     break
        unitCount = 0
        for char in word:
            try:
                glyphWidth = f[char].width
            except:
                try:
                    gname = glyphNamesForValues[char]
                    glyphWidth = f[gname].width
                except:
                    glyphWidth = 0
            unitCount += glyphWidth
        # # add kerning
        # for i in range(len(word)-1):
        #     pair = list(word[i:i+2])
        #     unitCount += int(findKerning(pair))
        if units-tolerance <= unitCount <= units+tolerance:
            print(word)
            prints = prints - 1
        if wordlist.index(word) == len(wordlist)-1:
            print("Couldn't find anything!")
            break        

##### FUNCTION CALL ##############################################

sortWordsByWidth(randomly(usercase), wordwidth, numofwords)

##### THE END! ###################################################
