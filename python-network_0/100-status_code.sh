#!/bin/bash
# A script that sends a GET request to URL and displays the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
