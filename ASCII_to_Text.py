# ASCII to text conversion Game
# Author - Noah Grant
# Language - Python
# Instructions:
# 1. Enter a list of numbers seperated by spaces
# 2. Program will convert ASCII values into chatacters and display them 

message = []
exitMenu = False
ASCII_list = []
# loop through code
while not exitMenu:

    # Get User input
    ASCII_list.clear()
    ASCII_Input = input("Enter the list of ASCII values: ")

    # exit the loop
    if ASCII_Input.lower() == "exit":
        exitMenu = True
        print("Exiting Program")
        break

    # process string into list of int
    ASCII_Input = ASCII_Input.split(" ")

    # convert to int and catch errors
    for item in ASCII_Input:
        try:
            ASCII_list.append(int(item))
        except ValueError:
            print("Invalid Symbol. Please Enter Again")

    # display the list contents
    for item in ASCII_list:
        try:
            # limit to English ASCII characters
            print(chr(item))
        except ValueError:
            print("Invalid Range Must be between 0 and 255")
