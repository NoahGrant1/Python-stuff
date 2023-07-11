# guess the variable type game
# author - Noah Grant
# language - Python
# Program version 1
import random


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# game loop
loop = False
# question list and type of answer
questions = [("Enter an integer:", "int"),
             ("Enter a boolean: ", "bool"),
             ("Enter a float: ", "float"),
             ("Enter a string: ", "str")]
while not loop:
    # choose random question and get answer from user
    question = random.randint(0, len(questions) - 1)
    answer = input(questions[question][0])

    # Answer checking
    # check integer question
    if answer.isdigit() and questions[question][1] == "int":
        print("correct")
    # check float question
    elif answer.replace(".", "").isnumeric() and questions[question][1] == "float" \
            and is_int(answer) is False:
        print("correct")
    # check string question
    elif answer.isalpha() and questions[question][1] == "str":
        print("correct")
    # check boolean question
    elif answer.lower() == ("true" or "false") and questions[question][1] == "bool":
        print("correct")
    else:
        print("incorrect")

    # exit the loop
    if answer.lower() == "exit":
        print("Closing Program")
        loop = True
