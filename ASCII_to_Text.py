message = []
exitMenu = False
# loop through code
while not exitMenu:
    print("Enter the ASCII values one at a time and then type decode")
    selection = input("Enter the ASCII value: ")

    # Add to message list
    # check if numeric and within ASCII value range 
    if selection.isnumeric() and not int(selection) < 0 and not int(selection) > 255:
        message.append(int(selection))
    # display the decoded message
    elif selection.lower() == "decode":
        exitMenu = True
    else:
        print("Invalid Symbol. Please Enter Again")

# print the message
for char in message:
    print(chr(char))
