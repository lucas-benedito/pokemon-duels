#!/usr/bin/env python3
import random
import ast
import sys
import os.path
from os import path

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

if checkQuit:
    print(messageQuit)
    sys.exit(1)

# main
count=6
battle_type=['single', 'doubles']
print("========================\nBattle Type: ",random.choice(battle_type))
file = open("options.txt", "r")
content = file.read()
pokemon_dict = ast.literal_eval(content)
lists = random.sample(list(pokemon_dict), count)

print("========================\n" + competitor1 + ":")
for ids in lists:
    print(pokemon_dict[ids])

file = open("options2.txt", "r")
content = file.read()
pokemon_dict = ast.literal_eval(content)
lists = random.sample(list(pokemon_dict), count)

print("========================\n" + competitor2 + ":")
for ids in lists:
    print(pokemon_dict[ids])

print("========================\nHave Fun.\n========================")
