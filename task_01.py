#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a list of versus matchups for players"""


def get_matches(players):
    """Creates a list of versus matchups for players in a tournament

    Args:
        players(list): a list of player names.

    Returns:
        tuple: Players grouped together.

    Examples:
    >>> get_matches(['Harry', 'Howard', 'Hugh'])
    [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """
    matches = []
    theplayers = list(enumerate(players))
    for player1 in theplayers:
        for player2 in theplayers:
            if player1[0] < player2[0]:
                matches.append((player1[1], player2[1]))
    return matches
