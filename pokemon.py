#!/usr/bin/env python3
"""
Pokemon battle generator
"""
import random
import sys
import os
from os import path
import shutil
import pandas as pd
import tabulate
import inquirer


def can_run():
    """
    Function to define if we are able to run the code
    """
    check = False
    message_quit = "\n"
    competitor1 = ""
    competitor2 = ""

    # check fi the arguments were passed to the script
    if len(sys.argv) < 3:
        print(
            f"""
Missing competitors names.
Usage: {sys.argv[0]} competitor1 competitor2.\n\n
        """
        )
        check = True
    else:
        competitor1 = sys.argv[1]
        competitor2 = sys.argv[2]

    # check if options files exist
    for options in ["options.xls", "options2.xls"]:
        if not os.path.isfile(options):
            print(
                f"""
                The file {options} doesnt exist, please create it and run again.\n
            """
            )
            check = True

    # Check if the necessary directories exist
    if not os.path.isdir("sprites"):
        print(
            "The directory sprites doesnt exist. Please, \
create it and populate with the pokemon sprites.\n"
        )
        check = True

    if not os.path.isdir("team"):
        try:
            os.makedirs("team")
            # Check if score files exist
            for scores in ["score1.txt", "score2.txt"]:
                if not os.path.isfile("team" + PATH_DELIMITER + scores):
                    with open(
                        "team" + PATH_DELIMITER + scores, "w", encoding="utf-8"
                    ) as file:
                        file.write("0")
        except OSError as error:
            print("Failed to create dirs", error)

    # Check if the default sprite file exist
    if not os.path.isfile("sprites" + PATH_DELIMITER + "000.png"):
        print(
            "The default sprite named '000.png' doesn't exist in sprites folder. \
Please add it to the directory and try again.\n"
        )
        check = True

    # Quit script if any failure was encountered
    if check:
        print(message_quit)
        sys.exit(1)
    return competitor1, competitor2


def sum_scores(winner):
    """
    Function to save the scores
    """
    with open("team" + PATH_DELIMITER + winner + ".txt", "r", encoding="utf-8") as fout:
        sum_score = fout.read()
        sum_score = int(sum_score) + 1
    with open("team" + PATH_DELIMITER + winner + ".txt", "w", encoding="utf-8") as fout:
        fout.write(str(sum_score))


def read_score():
    """
    Read the current score and show to the user
    """
    score_return = []
    for score_file in ["score1", "score2"]:
        with open(
            "team" + PATH_DELIMITER + score_file + ".txt", "r", encoding="utf-8"
        ) as fout:
            score_return.append(fout.read())
    return score_return


def battle_type():
    """
    defining the battle type
    """
    # Set battle type
    b_type = ["single", "doubles"]
    b_type_choice = random.choice(b_type)
    with open(
        "team" + PATH_DELIMITER + "battleType.txt", "w", encoding="utf-8"
    ) as file:
        file.write(b_type_choice)
    print(f"Battle Type: {b_type_choice}\n")


def read_team(team_data, team):
    """
    Generate Team data
    """
    count = 6
    content = pd.read_excel(team_data[0], header=0)
    content = content.fillna("-")
    selected = random.sample(range(content["Dex"].count()), count)
    selected_data = content.loc[selected, ["Nome", "Apelido"]]
    count_loop = 1
    for ids in selected:
        message_out = tabulate.tabulate(selected_data, showindex=False)
        ids_it = len(str(content["Dex"].loc[ids]))
        dexid = str(content["Dex"].loc[ids])
        if ids_it < 3:
            if ids_it == 1:
                dexid = "00" + dexid
            else:
                dexid = "0" + dexid
            find_sprite(dexid, team, count_loop)
        count_loop += 1
    with open("team" + PATH_DELIMITER + team + ".txt", "w", encoding="utf-8") as file:
        file.write(message_out)
    print(f"Team {team_data[1]}: \n{message_out}")


def find_sprite(dexid, team, count_loop):
    """
    Manage sprites
    """
    if path.isfile("sprites" + PATH_DELIMITER + dexid + ".gif"):
        fformat = ".gif"
    else:
        fformat = ".png"
    src_folder = "sprites" + PATH_DELIMITER + dexid + fformat
    tgt_folder = "team" + PATH_DELIMITER + team + "P" + str(count_loop) + ".gif"
    if not path.isfile(src_folder):
        src_folder = "sprites" + PATH_DELIMITER + "000.png"
    try:
        shutil.copyfile(src_folder, tgt_folder)
    except OSError as error:
        print("Unable to copy file.\n", error)


def main():
    """
    Main function
    """
    competitor1, competitor2 = can_run()

    battle_type()

    my_players = {
        "T1": ["options.xls", competitor1],
        "T2": ["options2.xls", competitor2],
    }
    for team in ["T1", "T2"]:
        read_team(my_players[team], team)

    questions = [
        inquirer.List(
            "score", message="Who won the fight?", choices=["Team 1", "Team 2"]
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers["score"] == "Team 1":
        sum_scores("score1")
    else:
        sum_scores("score2")
    current_score = read_score()
    print(
        f"Current Score: \n\
{my_players['T1'][1]}: {current_score[0]}\n\
{my_players['T2'][1]}: {current_score[1]}\n"
    )

    print("Have Fun.")


if __name__ == "__main__":
    if sys.platform.startswith("win"):
        PATH_DELIMITER = "\\"
    else:
        PATH_DELIMITER = "/"
    main()
