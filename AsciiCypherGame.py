ASCII Cypher Game
# Declare empty list and get message from user
Ascii_values = []
message = input("Enter Sentence to display as ASCII: ")

# translate message into ASCII and display it
for char in message:
  Ascii_values.append(ord(char))
  print(Ascii_values)
