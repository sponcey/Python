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
    content_list_caps.append(word.upper())

content_list_sc = []
for word in content_list:
    content_list_sc.append(word.upper())
    
lists_zipped = zip(content_list, content_list_caps, content_list_sc)

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

# If external dict exists, save the font, 
if goldendict_look.exists():
    print("It exists!")
    ## If font was saved before generating new dict, use this dict.
    if os.path.getmtime(f.path) <= os.path.getmtime('lib/tempdict.txt'):
        print("No need to rewrite!")
        with open('lib/tempdict.txt', 'r') as inf:
            goldendict = eval(inf.read())
                 
    # If external dict doesn't fulfill the above, make one!
    else:
        f.save()
        goldendict.clear()
        # Function that takes the word list, and compiles a dictionary by first adding the word; then adding a list (or tuple?) of values 
        # based on the measured glyphWidth of lowercase, uppercase, and sentence case.
        ## Something isn't working!!   
        if f is not None:
            fontChars, glyphNames = fontCharacters(f)
            glyphNamesForValues = {fontChars[i]: glyphNames[i] for i in range(len(fontChars))}
        else:
            fontChars = []
            glyphNames = [] 
         
        # For every word in the list, measure its caps width, lower width, and sentence case list, and make that a list 
        # Problem: Function is going through each list from start to finish, and then moving to the next list. How do I get it to look at the first item
        # in the first list, then the first item in the second list, then the first item in the third list, then the second item in the first list...
        def LengthList(wordlist):
            for wordgroup in wordlist:
                WordLength = []
                for word in wordgroup:
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
                        WordLength.append(unitCount)
                    WordWidth(word)
        # Put that list and its corresponding word into the WordWidthDic
                    goldendict.update({word: WordLength})
        LengthList(lists_zipped)
        with open('lib/tempdict.txt', 'w') as tempdict:
            tempdict.write(json.dumps(goldendict))
        
for key,val in goldendict.items():
    print(val[0])
        