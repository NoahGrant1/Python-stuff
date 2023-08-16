# Simon Game
# Author: Noah Grant
# issues:
#   implement timed input?
#   clear user input box after checking answer

#  instructions:
#  use the GUI

from tkinter import *
import random


# global variables
class game_data:
    count = 1
    colours = ["red", "blue", "yellow", "green"]
    question = []
    max_count = 10
    correct_answer = ""


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


# display incorrect or correct based on user input
def check_answer_function(correct_answer: str):
    # correct answer
    if user_input.get(1.0, "end-1c") == correct_answer:
        message = display.create_text(50, 100, text="correct, increasing difficulty")
        # increase the difficulty via count if correct answer
        if game_data.count != game_data.max_count:
            game_data.count += 1
    # incorrect answer
    else:
        message = display.create_text(50, 50, text="Incorrect")

    # display message in game
    #game_data.correct_answer = ""
    user_input.delete(1.0, 'end')
    display.moveto(message, 50, 50)
    display.update()

    # remove message from screen
    display.after(2000, display.delete(message))
    display.update()


# Display each colour for 1 secs
def display_colour(question: list):
    # loop through colours and display for 1 sec
    for item in question:
        # display colour
        shape = display.create_rectangle(50, 0, 50, 0, outline=item, width=500)
        display.moveto(shape, 50, 50)
        display.update()

        # remove colour
        display.after(1000, display.delete(shape))
        display.update()


# GUI setup commands
root = Tk()
root.geometry("600x600")
root.title(" Simon Game ")
display = Canvas(root, width=200, height=150)

# game description
intro = Label(text="Welcome to the Simon Game \n"
                   "Enter first letter of each colour with no spaces e.g rgby, rrrr \n"
                   "Once Game is ended press exit to close the program. ")

# start the next round button
start_game = Button(root, height=2,
                    width=20,
                    text="Start",
                    command=lambda: generate_question())

# user input box
user_input = Text(root,
                  height=5,
                  width=20)

# check answer button and increase difficulty
check_answer_button = Button(root, height=2,
                             width=20,
                             text="Check Answer",
                             command=lambda: check_answer_function(game_data.correct_answer))

# end the game button
end_game = Button(root, height=2,
                  width=20,
                  text="End",
                  command=lambda: exit(0))


intro.pack()
start_game.pack()
user_input.pack()
display.pack()
check_answer_button.pack()
end_game.pack()
mainloop()

