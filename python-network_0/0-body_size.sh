#!/bin/bash
# A script that takes a URL, sends a request to itand displays the body size of the response.
curl -s "$1" | wc -c
