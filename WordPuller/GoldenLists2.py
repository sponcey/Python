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

print(lists_zipped)