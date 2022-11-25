#!/usr/bin/env python3
import argparse
import sys

# define needed CLI
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help='file to create/edit')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value


# convert arg into variables
args = parser.parse_args()
print(args.filename, args.count)

# file manipulation
try:
    file = open(args.filename,"a")
except():
    print("File Opening error! ")
    sys.exit(1)
else:
    file.write("Hello World")
    file.close()

try:
    file = open(args.filename,"r")
except():
    print("File Opening error! ")
else:
    message = file.read()
    args.count = len(message)
    file.close()

print(f"The file contains: {message} \n which is: {args.count} long")

