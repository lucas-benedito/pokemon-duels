#!/usr/bin/env python3
import random
import sys
import os.path
from os import path
import shutil
import pandas as pd
import tabulate

# preliminary checks
# preliminary variables
checkQuit = False
messageQuit = "\n"

# check fi the arguments were passed to the script
if len(sys.argv) < 3:
    messageQuit = messageQuit + "Missing competitors names.\nUsage: " + sys.argv[0] + " competitor1 competitor2.\n\n"
    checkQuit = True
else:
    competitor1 = sys.argv[1]
    competitor2 = sys.argv[2]

for options in ['options.xls', 'options2.xls']:
    if not path.isfile(options):
        messageQuit = messageQuit + "The file " + options + " doesn't exist, please create it and run again.\n"
        checkQuit = True

# Check if the necessary directories exist
for directories in ['sprites', 'team']:
    if not os.path.isdir(directories):
        messageQuit = messageQuit + "The directory " + directories + " doesn't exist. Please, create it and populate with the pokémon sprites.\n "
        checkQuit = True

# Set path Delimiter depending on the platform
if sys.platform.startswith('win'):
    pathDelimiter = "\\"
else:
    pathDelimiter = '/'

# Check if the default sprite file exist
if not os.path.isfile('sprites' + pathDelimiter + '000.png'):
    messageQuit = messageQuit + "The default sprite named \'000.png\' doesn't exist in sprites folder. Please add it to the directory and try again. \n "
    checkQuit = True

# Quit script if any failure was encountered
if checkQuit:
    print(messageQuit)
    sys.exit(1)

# main
# Global Variables
count = 6
header = ["Dex", "Nome", "Apelido"]

# Set battle type
battle_type = ['single', 'doubles']
battle_type_choice = random.choice(battle_type)
print("Battle Type: " + battle_type_choice + "\n")
testDict = {'T1': ['options.xls', competitor1], 'T2': ['options2.xls', competitor2]}
for valueIteration in ['T1', 'T2']:
    messageOut = ""
    content = pd.read_excel(testDict[valueIteration][0], header=0)
    content = content.fillna('-')
    print(content['Dex'].count())
    lists = random.sample(range(content['Dex'].count()), count)
    a = content.loc[lists, ['Nome', 'Apelido']]
    countLoop = 1
    for ids in lists:
        messageOut = messageOut + "Team " + testDict[valueIteration][1] + ": \n"
        messageOut = tabulate.tabulate(a, showindex=False)
        original = 'sprites' + pathDelimiter + str(content['Dex'].loc[ids]) + '.png'
        target = 'team' + pathDelimiter + valueIteration + 'P' + str(countLoop) + '.png'
        print(original)
        if not os.path.isfile(original):
            original = 'sprites' + pathDelimiter + '000.png'
        shutil.copyfile(original, target)
        countLoop += 1
        file = open('team' + pathDelimiter + valueIteration + '.txt', 'w')
        file.write(messageOut)
        file.close
    print(messageOut)
    print()

print('Have Fun.')
