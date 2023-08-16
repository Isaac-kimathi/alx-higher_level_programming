#!/usr/bin/python3
#prints the result of the addition of all arguments
if __name__ == "__main__":
    import sys

    tgtr = 0
    for x in range(len(sys.argv) - 1):
        tgtr += int(sys.argv[x + 1)
    print("{}".format(tgtr))
