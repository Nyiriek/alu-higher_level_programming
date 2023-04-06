#!/usr/bin/python3
"""A script that
 fetches "https://alu-intranet.hbtn.io/status.
"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
	body = response.read()
	print("Body response:")
	print("\t- type: {}".format(type(body)))
	print("\t- content: {}".format(body))
	print("\t- utf8 content: {}".format(body.decode("utf-8")))
