#!/usr/bin/python3
"""
This module fetches a URL and displays information about the response body.
"""

import urllib.request


def fetch_status():
    """
    Fetches the Holberton intranet status page and prints details about the body.
    """
    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
