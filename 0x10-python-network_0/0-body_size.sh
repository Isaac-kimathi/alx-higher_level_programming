#!/bin/bash
# script send a http request, and displays the body size of response
curl -s "$1" | wc -c
