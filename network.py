#!urc/bin/env python3

import requests
import socket


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    # print("localhost = {}".format(localhost))
    return localhost == "127.0.0.1"

def check_connectivity():
    request = requests.get("http://www.google.com")
    status_code = request.status_code
    # print("Status code = {}".format(status_code))
    return status_code == 200
