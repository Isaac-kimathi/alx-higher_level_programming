#!/usr/bin/python3
# prints all the names defined by the compiled module hidden_4.pyc

if __name__ == "__main__":
    import hidden_4
    for x in dir(hidden_4):
        if x[:2] != "__":
            print("{:s}".format(x))
