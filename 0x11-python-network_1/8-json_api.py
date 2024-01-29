#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter"""
import sys
import requests

if __name__ == "__main__":
    ltr = "" if len(sys.argv) == 1 else sys.argv[1]
    upload = {"q": ltr}

    r = requests.post("http://0.0.0.0:5000/search_user", data=upload)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
