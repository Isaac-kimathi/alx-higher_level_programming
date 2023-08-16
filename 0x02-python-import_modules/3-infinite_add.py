#!/usr/bin/python3
#prints the result of the addition of all arguments

from sys import argv
tgtr = 0
for x in argv[1:]:
    tgtr += int(x)
    print("{:d}".format(tgtr))
