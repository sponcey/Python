# Using the Golden Ratio, start with a defined word width, and create a cascade of words from shortest to longest, across a certain amount of iterations.
## I need a function I can put in sortWordsByWidth that can define new lists based on changing variables.
### Scratch that. I should define a dictionary based on the list that measures the widths of the words. So every word has a value next to it that can be compared against the desired width. 

from __future__ import print_function
import random

f = CurrentFont()

def fontCharacters(font):
    if not font:
        return []
    charset = []
    gnames = []
    for g in font:
        if g.unicode is not None:
            try:
                charset.append(unichr(int(g.unicode)))
                gnames.append(g.name)
            except ValueError:
                pass
    return charset, gnames

text = open('lib/ukacd.txt', 'r')
content = text.read()
text.close()
list(content)

content_list = content.split('\n')
del content_list[0:25]
    
content_list_lc = []
for word in content_list:
    content_list_lc.append(word.lower())
    
WordWidthDic = {}

# Function that takes the word list, and compiles a dictionary by first adding the word; then adding a list of values based on the measured glyphWidth of lowercase, uppercase, and sentence case.

def MakeDic(wordlist):
    if f is not None:
        fontChars, glyphNames = fontCharacters(f)
        glyphNamesForValues = {fontChars[i]: glyphNames[i] for i in range(len(fontChars))}
    else:
        fontChars = []
        glyphNames = []
     
    # For every word in the list, measure its caps width, lower width, and sentence case list, and make that a list
    ## Something isn't working!!    
    for word in wordlist:
        capsword = word.upper()
        lowerword = word.lower()
        scaseword = word.upper()
        WordLen = []
            
        def WordWidth(casedword):
            unitCount = 0
            for char in casedword:
                try:
                    glyphWidth = f[char].width
                except:
                    try:
                        gname = glyphNamesForValues[char]
                        glyphWidth = f[gname].width
                    except:
                        glyphWidth = 0
                unitCount += glyphWidth
            WordLen.append(unitCount)
        WordWidth(capsword)
        WordWidth(lowerword)
        WordWidth(scaseword)
        # Put that list and its corresponding word into the WordWidthDic
        WordWidthDic.update({word: WordLen})
        
MakeDic(content_list)
print(WordWidthDic.head(3))