#!/bin/bash
# A script that sends a POST request to the passed URL and displays the body of the response
curl -sXd POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
