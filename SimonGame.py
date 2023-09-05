# Simon Game
# Author: Noah Grant
# issues:
#  rework check function to accept nothing

from tkinter import *
import time
import random

class game_data:
    count = 1
    colours = ["red", "blue", "yellow", "green"]
    question = []
    max_count = 10
    correct_answer = ""
    user_answer = ""

# global variables
def clear_data():
    game_data.correct_answer = ""
    game_data.user_answer = ""

# reset the game difficulty to 1
def reset_diff():
    game_data.count = 1
    message = display.create_text(50, 100, text="reset difficulty")
    display.moveto(message, 50, 50)
    display.update()

    # remove message from screen
    display.after(2000, display.delete(message))
    display.update()


# generate a random combination of colours and expected answer
def generate_question():
    # empty list for each round
    game_data.question.clear()
    game_data.correct_answer = ""

    # generate random colours
    for item in range(game_data.count):
        game_data.question.append(random.choice(game_data.colours))

    # create shortened expected answer
    game_data.correct_answer = [item[0] for item in game_data.question]  # extract first letter from list
    game_data.correct_answer = ''.join(game_data.correct_answer)  # make list into string
    game_data.correct_answer = ''.join(e for e in game_data.correct_answer if e.isalpha())  # purge space

    # display the question
    display_colour(game_data.question)


# Display each colour for 1 secs
def display_colour(question: list):
    # loop through colours and display for 1 sec
    for item in question:
        # display colour
        shape = display.create_rectangle(50, 0, 50, 0, outline=item, width=500)
        display.moveto(shape, 50, 50)
        display.update()

        # remove colour and delay next colour
        display.after(1000, display.delete(shape))
        display.update()
        time.sleep(0.5)


# use 4 buttons for input
def check_answer_function(colour: str):
    # If all colours selected then proceed
    if len(game_data.user_answer) == game_data.count:
        # correct answer
        if game_data.user_answer == game_data.correct_answer:
            message = display.create_text(50, 100, text="correct, increasing difficulty")
            clear_data()
            # increase the difficulty via count if correct answer
            if game_data.count != game_data.max_count and colour != "":
                game_data.count += 1
        # incorrect answer
        else:
            message = display.create_text(50, 50, text="Incorrect")
            clear_data()

        # display message in game
        display.moveto(message, 50, 50)
        display.update()

        # remove message from screen
        display.after(2000, display.delete(message))
        display.update()

    # Add new character to existing answer
    else:
        game_data.user_answer += colour


# GUI setup commands
root = Tk()
root.geometry("500x500")
root.title(" Simon Game ")
root.configure(bg='gray')
display = Canvas(root, width=200, height=150)
display.configure(bg='gray', highlightbackground='black')

# game description
intro = Label(text="Welcome to the Simon Game \n"
                   "Click start and enter the sequence of colours used the buttons \n"
                   "Press check Button when done to reveal result",
              bg="gray")

# start the next round button
start_game = Button(root, height=2, width=20, text="Start",
                    command=lambda: generate_question(), bg='slategray4')

# end the game button
end_game = Button(root, height=2, width=20, text="End",
                  command=lambda: exit(0), bg='slategray4')

# check the user inputted answer
check_answer_button = Button(root, height=2, width=20, text="Check"
                             , command=lambda: check_answer_function(""), bg='slategray4')

# reset difficulty  button
reset_difficulty = Button(root, height=2, width=20, text="Reset Difficulty"
                          , command=lambda: reset_diff(), bg='slategray4')

# buttons for user input
red_button = Button(root, bg=game_data.colours[0], width=20,
                    command=lambda: check_answer_function("r"))
blue_button = Button(root, bg=game_data.colours[1], width=20,
                     command=lambda: check_answer_function("b"))
yellow_button = Button(root, bg=game_data.colours[2], width=20,
                       command=lambda: check_answer_function("y"))
green_button = Button(root, bg=game_data.colours[3], width=20,
                      command=lambda: check_answer_function("g"))

# GUI design
intro.grid(row=0, column=1, sticky=W, pady=2, columnspan=3)
start_game.grid(row=1, column=1, sticky=W, pady=2, columnspan=3)
display.grid(row=2, column=1, sticky=W, pady=2, columnspan=3)
red_button.grid(row=4, column=1, sticky=W, pady=2, columnspan=3)
blue_button.grid(row=6, column=1, sticky=W, pady=2, columnspan=3)
check_answer_button.grid(row=5, column=1, sticky=W, pady=2, columnspan=1)  # centre of controls
yellow_button.grid(row=5, column=0, sticky=W, pady=2, columnspan=1)
green_button.grid(row=5, column=2, sticky=W, pady=2, columnspan=1)
reset_difficulty.grid(row=7, column=1, sticky=W, pady=2, columnspan=3)
end_game.grid(row=8, column=1, sticky=W, pady=2, columnspan=3)
mainloop()
