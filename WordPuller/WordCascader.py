## WordCascader creates a function that, using three inputs (list, word width in units, number of words) generates a lists of perfectly justified words when set in the currently opened font. Pretty nifty! Much of the code is taken from Word-o-mat by Nina Stoessinger. <3

# GOAL: Generate lists of words based on currently open typeface. Ideally, I should be able to generate a list of words at different lengths in one script.
# Current problem: Can't figure out way of doing it that isn't extremely inefficient. best solution so far is to run thru the entire dictionary and measure the length of every single word and see if if it fulfills the requested parameters. Seems silly to take the entire dictionary and measure EVERY single word.
# What if instead, it randomly chose a word, measure it to see if it fulfills any of the desired parameters, and then pops it from the list. Once it finds as many words as are needed, it stops. If the script pops all words from the list, it stops.
# Is there a way to input multiple parameters? so the number of inputs change?
# Is there a way to output text so it's already marked up with CSS/Indesign Markup?
# Script would generate a function for every additional variable.

import random

# Import dictionary as list
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
    content_list_sc.append(word.capitalize())
    
f = CurrentFont()

#Check which unicode characters are available in the font.
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
        
# # Helper function to find kerning between two given glyphs.
# # This assumes MetricsMachine style group names.
# def findKerning(chars):
#     markers = ["@MMK_L_", "@MMK_R_"]
#     keys = [c for c in chars]

#     for i in range(2):
#         allGroups = f.groups.findGlyph(chars[i])
#         if len(allGroups) > 0:
#             for g in allGroups:
#                 if markers[i] in g:
#                     keys[i] = g
#                     continue

#     key = (keys[0], keys[1])
#     if f.kerning.has_key(key):
#         return f.kerning[key]
#     else:
#         return 0

# Function taken from Word-o-mat to look at words widths
# Problem currently: Script is taking forever to load because it is 
def sortWordsByWidth(wordlist, units, prints):
    wordWidths = []
    if f is not None:
        fontChars, glyphNames = fontCharacters(f)
        glyphNamesForValues = {fontChars[i]: glyphNames[i] for i in range(len(fontChars))}
    else:
        fontChars = []
        glyphNames = []
            
    for word in wordlist:
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
            wordWidths.append(word)
    while True:
        if len(wordWidths) <=1:
            print("I couldn't find anything!")
            break
        print(random.choice(wordWidths))
        if prints != 0:
            prints = prints-1
        if prints == 0:
            break
    
sortWordsByWidth(content_list_sc, 2000, 50)
