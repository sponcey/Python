import random

f = CurrentFont()

# Read external text file and make it a list.
text = open('lib/ukacd.txt', 'r', encoding='latin1')
content = text.read()
text.close()
list(content)
content_list = content.split('\n')
del content_list[0:25]

# Path to Dictionary
goldendict_look = Path("lib/goldendict.txt")

# Function that defines list of characters in font
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

# If external dict exists, read it and convert to dict.
if goldendict_look.exists():
    goldendict = {}
    with open('lib/goldendict.txt', encoding='latin1') as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val
            
# If external dict doesn't exist, make one!
else:
    goldendict = {}
    # Function that takes the word list, and compiles a dictionary by first adding the word; then adding a list (or tuple?) of values 
    # based on the measured glyphWidth of lowercase, uppercase, and sentence case.
        ## Something isn't working!!   
    def MakeDic(wordlist):
        if f is not None:
            fontChars, glyphNames = fontCharacters(f)
            glyphNamesForValues = {fontChars[i]: glyphNames[i] for i in range(len(fontChars))}
        else:
            fontChars = []
            glyphNames = []
     
        # For every word in the list, measure its caps width, lower width, and sentence case list, and make that a list 
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
# Biggest problem: Script is taking FOREVER 

# Current Script: Go through and measuring the length of ALL WORDS, and make a list of words that are the desired LENGTH.

# Better Script: 
# FIRST: check to see if a temporary folder /resources/ exists in the root of the script. 
# If it does, continue. 
# If it doesn't, create a temp folder.
# SECOND: Check to see if a temp dictionary of word length values exists in /resources/. 
# If it doesn't, generate a dictionary containing the lengths of the words, and export that dictionary to /resources/. then print "New Dictionary Generated!"
# If it does, then:
    # Check to see if the font has been modified since the dictionary was generated. If it was, overwrite the old dict, and print "Dict Overwritten!"
    # If the font hasn't been modified since the dictionary was generated, then continue.