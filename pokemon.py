#!/usr/bin/env python3
import random
import ast
import sys
import os.path
from os import path
import shutil


# preliminary checks
checkQuit = False
messageQuit = "\n"
if len(sys.argv) < 3:
    messageQuit = messageQuit + "Missing competitors names.\nUsage: " + sys.argv[0] + " competitor1 competitor2.\n\n"
    checkQuit = True
else:
    competitor1 = sys.argv[1]
    competitor2 = sys.argv[2]

for options in ['options.txt','options2.txt']:
    if not path.isfile(options):
        messageQuit = messageQuit + "The file " + options + " doesn't exist, please create it and run again.\n"
        checkQuit = True

for directories in ['sprites', 'team']:
    if not os.path.isdir(directories):
        messageQuit = messageQuit + "The directory " + directories + " doesn't exist. Please, create it and populate with the pokémon sprites.\n"
        checkQuit = True

if checkQuit:
    print(messageQuit)
    sys.exit(1)

if sys.platform.startswith('win'):
    pathDelimiter = "\\"
else:
    pathDelimiter = '/'

# main
count=6
messageSplit = '========================\n'
battle_type=['single', 'doubles']
print(messageSplit + "Battle Type: ",random.choice(battle_type) + "\n" + messageSplit)

testDict = {'T1':['options.txt',competitor1], 'T2':['options2.txt',competitor2]}
for valueIteration in ['T1', 'T2']:
    messageOut = ""
    file = open(testDict[valueIteration][0], "r")
    content = file.read()
    file.close()
    pokemon_dict = ast.literal_eval(content)
    lists = random.sample(list(pokemon_dict), count)
     
    messageOut = messageOut + "Team " + testDict[valueIteration][1] + ": \n"
    countLoop = 1
    for ids in lists:
        messageOut = messageOut + (pokemon_dict[ids][0]) + "\n"
        fileFormat = pokemon_dict[ids][2]
        original = 'sprites' + pathDelimiter + pokemon_dict[ids][1] + fileFormat
        target = 'team' + pathDelimiter + valueIteration + 'P' + str(countLoop) + '.gif'
        if not os.path.isfile(original):
            original = 'sprites' + pathDelimiter + '000.png'
        shutil.copyfile(original, target)
        countLoop += 1
        file = open('team' + pathDelimiter + valueIteration + '.txt', 'w')
        file.write(messageOut)
        file.close
    print(messageOut + messageSplit)

print('Have Fun.')
