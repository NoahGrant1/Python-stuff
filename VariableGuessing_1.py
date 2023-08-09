# guess the variable type game
# author - Noah Grant
# language - Python
# Program version 1
# Programs supports integer, float, 5boolean, dictionary, list, and string.
# added extra questions is done by adding it to the questions list
# and adding a new check condition in the answer checking section.
import random


# check if a value is an integer and return bool statement
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# turn answer into a list
def make_list(value):
    # make sure string type and split at space
    value = str(value)
    value = value.split(" ")
    return value


# turn answer into a dictionary
def make_dict(value):
    # get user input and seperate key and value
    value = str(value)
    try:
        value = value.split(":")
    except ValueError:
        return False

    # make the dictionary and assign key and value
    temp = dict()
    if len(value) >= 2:
        temp[value[0]] = value[1]
        return temp

    return False


# game loop
loop = False
# question list and type of answer
questions = [("Enter an integer:", "int"),
             ("Enter a boolean: ", "bool"),
             ("Enter a float: ", "float"),
             ("Enter a string: ", "str"),
             ("Enter a list: (separate items with space) ", "list"),
             ("Enter a dictionary: (separate items with : )", "dict")]
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
    # check string question - replaces punctuation with characters to pass check
    # make empty string and only add alpha characters
    elif ''.join(e for e in answer if e.isalpha()) and questions[question][1] == "str":
        print("correct")
    # check boolean question
    elif answer.lower() == "true" or "false" and questions[question][1] == "bool":
        print("correct")
    # check list question
    elif questions[question][1] == "list":
        # if more than 2 elements and determine respond with answer
        if len(make_list(answer)) >= 2:
            print("correct")
        else:
            print("incorrect")
    # check dictionary questions
    elif questions[question][1] == "dict":
        # check type supplied from user and compare  - add try and catch errors
        if type(make_dict(answer)) is dict:
            print("correct")
        else:
            print("incorrect")
    else:
        print("incorrect")

    # exit the loop
    if answer.lower() == "exit":
        print("Closing Program")
        loop = True
