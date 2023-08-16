#!/usr/bin/python3
# prints the number of and the list of its arguments
if __name__ == "__main__":

    import sys

    tally = len(sys.argv) - 1
    if tally == 0:
        print("0 arguments.".)
    elif tally == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(tally))
    for x in range(tally):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
