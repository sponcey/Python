## Golden Lists 2 ##

import random, json, os, time
from pathlib import Path

f = CurrentFont()

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

def randomly(seq):
    shuffled = list(seq)
    random.shuffle(shuffled)
    return shuffled
        
lists_zipped = list(zip(content_list, content_list_caps, content_list_sc))

# Path to Dictionary
goldendict_look = Path('lib/tempdict.txt')
goldendict = {0:1, 2:3}

# Function that defines list of characters in font
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

# usercase = input("all lower, Capitalized, or ALL CAPS? ")
# userwidth = input("How many units wide? ")


def sortWordsByWidth(wordlist, units, prints):
    if f is not None:
        fontChars, glyphNames = fontCharacters(f)
        glyphNamesForValues = {fontChars[i]: glyphNames[i] for i in range(len(fontChars))}
    else:
        fontChars = []
        glyphNames = []
    
    # This for loop is eating up SO MUCH PROCESSING TIME. Is there a simpler way to write this to get a quicker result? Do I really need
    # it to measure EVERY SINGLE word in the dictionary?
    printcounter = prints     
    for word in wordlist:
        if printcounter >= 1 and len(wordlist) >= 1:
            continue
        elif printcounter == 0 or len(wordlist) == 0:
            print ("Couldn't find anything!")
            break
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
        if units-50 <= unitCount <= units+50:
            print(word)
            printcounter -= 1
        wordposition = wordlist.index(word)
        del wordlist[wordposition]
        if len(wordlist) == 0:
            print("Couldn't find anything!")
        

        # if len(wordWidths) == 0:
        #     print("I couldn't find anything!")
        # elif len(wordWidths) >= 1:
        #     print(len(wordWidths))
        #     while prints != 0:
        #         print(random.choice(wordWidths))
        #         prints = prints-1
        #     else:
        #         print("All done!")

sortWordsByWidth(randomly(content_list_sc), 3000, 5)


