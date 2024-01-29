#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id"""
import sys
import requests

if __name__ = "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = f"https://api.github.com/users/{Isaac-Kimathi}"
    headers = {"Authorization": f"token {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}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get("id")
        print("Your GitHub ID:", user_id)
    else:
        print("Error:", response.status_code)
