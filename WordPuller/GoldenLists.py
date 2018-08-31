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

# Path to Dictionary
goldendict_look = Path('lib/tempdict.txt')
goldendict = {1:2, 2:3}

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

# If external dict exists, save the font, 
if goldendict_look.exists():
    print("It exists!")
    f.save()
    ## If font was saved before generating new dict, use this dict.
    # if os.path.getmtime(f.path) <= os.path.getmtime(goldendict_look):
    with open('lib/tempdict.txt', 'r') as inf:
        goldendict = eval(inf.read())
            
# # If external dict doesn't fulfill the above, make one!
# else:
#     f.save()
#     # Function that takes the word list, and compiles a dictionary by first adding the word; then adding a list (or tuple?) of values 
#     # based on the measured glyphWidth of lowercase, uppercase, and sentence case.
#     ## Something isn't working!!   
#     if f is not None:
#         fontChars, glyphNames = fontCharacters(f)
#         glyphNamesForValues = {fontChars[i]: glyphNames[i] for i in range(len(fontChars))}
#     else:
#         fontChars = []
#         glyphNames = []
 
#     # For every word in the list, measure its caps width, lower width, and sentence case list, and make that a list 
#     def DictGen(wordlist):
#         for word in wordlist:
#             capsword = word.upper()
#             lowerword = word.lower()
#             scaseword = word.upper()
#             WordLen = []
        
#             def WordWidth(casedword):
#                 unitCount = 0
#                 for char in casedword:
#                     try:
#                         glyphWidth = f[char].width
#                     except:
#                         try:
#                             gname = glyphNamesForValues[char]
#                             glyphWidth = f[gname].width
#                         except:
#                             glyphWidth = 0
#                     unitCount += glyphWidth
#                 WordLen.append(unitCount)
#             WordWidth(capsword)
#             WordWidth(lowerword)
#             WordWidth(scaseword)
#             # Put that list and its corresponding word into the WordWidthDic
#             goldendict.update({word: WordLen})
#     DictGen(content_list)
#     with open('lib/tempdict.txt', 'w') as tempdict:
#         tempdict.write(json.dumps(goldendict))
        
print(goldendict[1])
        