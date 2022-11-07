# TODO add input verification

# validate input is int and display provided prompt
def validation(displaymessage):
    while True:
        try:
            value = int(input(displaymessage))
            break
        # if user enters not a number
        except ValueError:
            print("Invalid Input")
    return value

def message():
    # validate user input
    count = validation("Enter the number of messages? ")

    # print hello and a final goodbye
    for i in range(count):
        print("hello world")
        if i == count - 1:
            print("goodbye")


def makelist():
    # make the list
    words = []
    # validate input
    number = validation("Enter the number of words")

    # add words to list
    for i in range(number):
        words.append(str(input("Enter a word: ")))

    # display the list
    return words


# menu item selection
exitMenu = False
while not exitMenu:
    print(" 1: welcome message \n 2: word list  \n 3: ...  \n 9. exit \n")
    # validate input
    selection = validation("Enter the Menu item: ")

    # menu selection code
    if selection == 1:
        # display welcome message
        message()
    elif selection == 2:
        # make a list of words
        print(makelist())
    elif selection == 9:
        # exit program
        exitMenu = True
        print("Quitting Program")
    else:
        print("Invalid Command")
