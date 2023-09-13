#!/usr/bin/python3
"""The module adds all arguments to a Python list and save them to a file.""" 

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_save_pylist(args_list):
    try:
        existing_items = load_from_json_file("add_items.json")
    except FileNotFoundError:
        existing_items = []

    for arg in args_list:
        existing_items.append(arg)

    save_to_json_file(existing_items, "add_items.json")

if __name__ == "__main__":
    avs = sys.argv[1:]

    add_save_pylist(avs)

