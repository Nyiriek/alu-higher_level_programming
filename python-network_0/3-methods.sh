#!/bin/bash
# Ascript that takes in a URL and displays all HTTP methods the server accepts
curl -sIX OPTIONS "$1" | grep "Allow" | cut -d " " -f 2- 
