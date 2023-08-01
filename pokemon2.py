#!/usr/bin/env python3
import random
import sys
import os
from os import path
import shutil
import pandas as pd
import tabulate
import inquirer

# preliminary checks
# preliminary variables
checkQuit = False
messageQuit = "\n"

# check fi the arguments were passed to the script
if len(sys.argv) < 3:
    messageQuit = (
        messageQuit
        + "Missing competitors names.\nUsage: "
        + sys.argv[0]
        + " competitor1 competitor2.\n\n"
    )
    checkQuit = True
else:
    competitor1 = sys.argv[1]
    competitor2 = sys.argv[2]

# Set path Delimiter depending on the platform
if sys.platform.startswith("win"):
    pathDelimiter = "\\"
else:
    pathDelimiter = "/"

# check if options files exist
for options in ["options.xls", "options2.xls"]:
    if not os.path.isfile(options):
        messageQuit = (
            messageQuit
            + "The file "
            + options
            + " doesnt exist, please create it and run again.\n"
        )
        checkQuit = True

# Check if the necessary directories exist
for directories in ["sprites", "team"]:
    if not os.path.isdir(directories):
        messageQuit = (
            messageQuit
            + "The directory "
            + directories
            + " doesnt exist. Please, create it and populate with the pokemon sprites.\n "
        )
        checkQuit = True

# Check if score files exist
for scores in ["score1.txt", "score2.txt"]:
    if not os.path.isfile("team" + pathDelimiter + scores):
        fin = open("team" + pathDelimiter + scores, "w+")
        fin.write("0")
        fin.close()

# Check if the default sprite file exist
if not os.path.isfile("sprites" + pathDelimiter + "000.gif"):
    messageQuit = (
        messageQuit
        + "The default sprite named '000.png' doesn't exist in sprites folder. Please add it to the directory and try again. \n "
    )
    checkQuit = True

# Quit script if any failure was encountered
if checkQuit:
    print(messageQuit)
    sys.exit(1)


def sumScores(winner):
    fout = open("team" + pathDelimiter + winner + ".txt", "rt")
    scoreSum = fout.read()
    fout.close()
    scoreSum = int(scoreSum)
    print(scoreSum)
    scoreSum += 1
    print(scoreSum)
    fout = open("team" + pathDelimiter + winner + ".txt", "w+")
    fout.write(str(scoreSum))
    fout.close()


def main():
    # main
    # Global Variables
    count = 6
    header = ["Dex", "Nome", "Apelido"]

    # Set battle type
    battle_type = ["single", "doubles"]
    battle_type_choice = random.choice(battle_type)
    print("Battle Type: " + battle_type_choice + "\n")
    file = open("team" + pathDelimiter + "battleType.txt", "w")
    file.write(battle_type_choice)
    file.close
    testDict = {"T1": ["options.xls", competitor1], "T2": ["options2.xls", competitor2]}
    for valueIteration in ["T1", "T2"]:
        messageOut = ""
        content = pd.read_excel(testDict[valueIteration][0], header=0)
        content = content.fillna("-")
        lists = random.sample(range(content["Dex"].count()), count)
        a = content.loc[lists, ["Nome", "Apelido"]]
        countLoop = 1
        for ids in lists:
            messageOut = messageOut + "Team " + testDict[valueIteration][1] + ": \n"
            messageOut = tabulate.tabulate(a, showindex=False)
            x = len(str(content["Dex"].loc[ids]))
            dexid = str(content["Dex"].loc[ids])
            if x < 3:
                if x == 1:
                    dexid = "00" + dexid
                else:
                    dexid = "0" + dexid
            original = "sprites" + pathDelimiter + dexid + ".gif"
            if path.isfile(original):
                fformat = ".gif"
            else:
                fformat = ".png"
                original = "sprites" + pathDelimiter + dexid + fformat
            target = "team" + pathDelimiter + valueIteration + "P" + str(countLoop) + ".gif"
            if not path.isfile(original):
                original = "sprites" + pathDelimiter + "000.gif"
            shutil.copyfile(original, target)
            countLoop += 1
            file = open("team" + pathDelimiter + valueIteration + ".txt", "w")
            file.write(messageOut)
            file.close
        print(messageOut)
    questions = [
        inquirer.List("score", message="Who won the fight?", choices=["Team 1", "Team 2"]),
    ]
    answers = inquirer.prompt(questions)
    if answers["score"] == "Team 1":
        sumScores("score1")
    else:
        sumScores("score2")

    print("Have Fun.")

if __name__ == "__main__":
    main()