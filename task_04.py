#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module compares kittens, litterboxes and catfood."""


def too_many_kittens(kittens, litterboxes, catfood):

    """game of kitten, litter boxes and food.

    Args:
        kittens (int): the number of kittens.
        litterboxes (int): the number of available litterboxes.
        catfood (boolean): weather or not any catfood exits.

    Returns:
        str: all arguments

    Examples:
        >>> too_many_kittens(12, 2, False)
        False
        >>> too_many_kittens (2, 13, True)
        True

    """
    animal = litterboxes >= kittens and catfood
    return animal
