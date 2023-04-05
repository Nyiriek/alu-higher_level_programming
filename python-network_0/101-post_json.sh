#!/bin/bash
# A script that sends a JSON POST to a URL and passed as an argument.
curl -sH "Content-Type: application/json" -d "@$2" "$1"
