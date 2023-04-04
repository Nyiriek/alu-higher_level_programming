#!/bin/bash
# Script that sends a DELETE request to the URL passed as an argument and displays the body of the response.
curl -sX "$1" DELETE
