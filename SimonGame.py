# Simon Game
# Author: Noah Grant
# issues:
#   Main Process requires user input to exit - unfixable
#   print colours temporarily with tkinter
#  instructions:
#  Enter first letter of the colours with no spaces between them
#  Program will end but not close without the user pressing enter.

import msvcrt
import random
import sys
from threading import Timer

# global variables
exit_menu = False
count = 1
colours = ["red", "blue", "yellow", "green"]
question = []
max_count = 10

# check the user enters the correct answer
def check(answer, expected_answer):
    result = False
    if answer == expected_answer:
        result = True
    return result

# end the game
def end_game():
    if alarm.is_alive():
        global exit_menu
        exit_menu = True
        print("\nToo slow ending Game")


print("Welcome to the Simon Game \n"
      "Enter first letter of each colour with no spaces e.g rgby, rrrr \n"
      "Once Game is ended press enter to close the program. ")

# Main loop
while exit_menu is not True:

    # empty list for each loop
    question.clear()

    # generate random colours
    for item in range(count):
        question.append(random.choice(colours))

    # create shortened expected answer
    correct_answer = [item[0] for item in question]  # extract first letter from list
    correct_answer = ' '.join(correct_answer)  # make list into string
    correct_answer = ''.join(e for e in correct_answer if e.isalpha())  # purge space

    # get user input
    print(question)  # send question to interface function

    # set the time limit and load function into thread
    alarm = Timer(10, lambda: end_game())

    # timed section
    alarm.start()
    answer = input("Enter the colour sequence: ").lower()
    alarm.cancel()

    # exit the game or close timing process
    if exit_menu is True:
        break

    # increase the difficulty via count if correct answer
    if check(answer, correct_answer) is True:
        if count != max_count:
            count += 1
        print("Correct")
    else:
        print("Wrong Answer or Order")
