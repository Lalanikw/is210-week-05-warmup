#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """this doc string strips winks and nudget and return retstr in a format.

    Args:
        wink (mixed): wink * by numwink.
        numwink (int): input. default '2'

    Returns:
        str: all arguments concatenated with commas.

    exampls:
        >>>know_what_i_mean (hello, 2)
        'Know what I mean? hello, 2'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
