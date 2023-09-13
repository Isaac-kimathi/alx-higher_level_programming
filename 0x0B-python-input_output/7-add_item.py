#!/usr/bin/python3
"""The module adds all arguments to a Python list and save them to a file.""" 

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        argvs = load_from_json_file("add_item.json")
    except FileNotFoundError:
        argvs = []
    argvs.extend(sys.argv[1:])
    save_to_json_file(argvs, "add_item.json")
