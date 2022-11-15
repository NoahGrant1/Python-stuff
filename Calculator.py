# Calculator
# Accepts user input and validates it
#!/usr/bin/env python3
# validate input is int and display provided prompt
def intvalid(rawvalue):
    while True:
        try:
            value = int(rawvalue)
            break
        # if user enters not a number
        except ValueError:
            print("Invalid Input")
    return value


# validare  input is str and display prompt
def strvalid(displaymessage):
    global ops
    while True:
        try:
            rawinput = str(input(displaymessage))
            break
        # if user enters not a number
        except ValueError:
            print("Invalid Input")

    # exit the calculator
    if rawinput == "exit":
        return rawinput

    # process input into parts
    input1 = ""
    input2 = ""
    input3 = ""
    for i in range(0, len(rawinput)):
        # get first number
        if rawinput[i] not in ops and input2 == "":
            input1 += rawinput[i]

        # get symbol
        if rawinput[i] in ops:
            input2 = rawinput[i]

        # get second number
        if rawinput[i] not in ops and input2 in ops:
            input3 += rawinput[i]

    # store the equation parts and return to main
    temp = (intvalid(input1), input2, intvalid(input3))
    return temp


def add(input1, input2):
    return input1 + input2


def sub(input1, input2):
    return input1 - input2


def div(input1, input2):
    if input2 == 0:
        return "Error: Divisor cannot be 0"
    return input1 / input2


def mul(input1, input2):
    return input1 * input2


def main():
    # menu item selection
    exitMenu = False
    global ops
    ops = ("+", "-", "/", "*")
    while not exitMenu:
        # validate input
        selection = strvalid("Enter the equation: (x+y) ")
        print(selection)

        # menu selection code
        if selection[1] in (ops[0]):
            # addition
            print(add(intvalid(selection[0]), intvalid(selection[2])))
        elif selection[1] in (ops[1]):
            # subtraction
            print(sub(intvalid(selection[0]), intvalid(selection[2])))
        elif selection[1] in (ops[2]):
            # division
            print(div(intvalid(selection[0]), intvalid(selection[2])))
        elif selection[1] in (ops[3]):
            # multiply
            print(mul(intvalid(selection[0]), intvalid(selection[2])))
        elif selection == "exit":
            # exit program
            exitMenu = True
            print("Quitting Program")
        else:
            print("Invalid Command")


# Run the main function
if __name__ == "__main__":
    main()
