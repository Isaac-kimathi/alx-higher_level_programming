#!/usr/bin/python3
"""Script sends a POST request to a given URL with a given email
usage: ./6-post_email.py <URL> <email>
Displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    result = requests.post(url, data=value)
    print(result.text)
