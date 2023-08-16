#!/usr/bin/python3
# prints the number of and the list of its arguments
def arg_lst(argv)

tally = len(.argv) - 1
if tally == 0:
    print("{:d} arguments.".format(tally))
    return
else:
    if tally == 1:
        print("{:d} arguments:".format(tally))
    else:
        print("{:d} arguments:".format(tally))
        x = 1
        while x <= n:
            print("{:d}: {:s}".format(x, argv[x]))
            x += 1
    if __name__ == "__main__":
        import sys
        arg_lst(sys.argv)
