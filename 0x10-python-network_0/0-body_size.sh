#!/usr/bin/python3
# script send a http request to URL, and displays the body size of response
curl -s "$1" | wc -c
