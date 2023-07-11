# input ASCII values and display decoded message
message = []
exitMenu = False
while not exitMenu:
   print("Enter the ASCII values one at a time and then type decode")
   selection = input("Enter the ASCII value: ")

# Add to message list
if selection.isnumeric():
    message.append(int(selection))
# display the decoded message
 elif selection.lower() == "decode":
    exitMenu = True

# print the message
 for char in message:
    print(chr(char))
 else:
    print("Invalid Symbol. Please Enter Again")
