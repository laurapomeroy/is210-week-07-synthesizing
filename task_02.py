#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Login authentication"""


import getpass
import authentication


def login(username, maxattempts=3):
    """Login authentication. Gives a few attempts befor locking you out.

    Args:
        username(str): A string representing the username of the user
        attempting to log in.
        maxattempts(int, optional): An integer represent of the maximum
        number of promted attempes.

    Examples:
        >>>login('Mike', 3)
        >>>Please enter your password:
        Incorrect username and password. You have 3 attempts left.
        Please enter your password:
        Incorrect username and password. You have 2 attempts left.
        Please enter your password:
        Incorrect username and password. You have 1 attempts left.
        Please enter your password:
        Incorrect username and password. You have 0 attempts left.
        False
    """
    count = 0
    please = 'Please enter your password:'
    failedlogin = 'Incorrect username and password. You have {} attempts left.'
    authenticated = False
    while not authenticated and count < maxattempts:
        password = getpass.getpass(please)
        if authentication.authenticate(username, password) is True:
            authenticated = True
        else:
            count += 1
            print failedlogin.format(maxattempts - count)
    return authenticated
