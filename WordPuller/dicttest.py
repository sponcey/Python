import json

testdict = {'garbage': [10,5,6], 'eulogy': [11,6,7], 'frederick': [100,40,30]}

# Prints the first item in the list from the value
for key,val in testdict.items():
    print(val[0])

# Writes the dictionary to file    
with open('lib/tempdict.txt', 'w') as tempdict:
    tempdict.write(json.dumps(testdict))
    
# Reads the dictionary file back and converts to dictionary in python.
with open('lib/tempdict.txt', 'r') as inf:
    dict_from_file = eval(inf.read())


for key,val in dict_from_file.items():
    print(val[2])