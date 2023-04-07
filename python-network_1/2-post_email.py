#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import argv from sys
from urllib import request, parse


if __name__ == "__main__":
    post_email()


def post_email():
    """Sends a POST request to the passed URL with the email as a parameter."""
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8") # The data should be in bytes

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
