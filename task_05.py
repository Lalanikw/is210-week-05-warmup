#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the task_05."""


def defaults(my_optional, my_required):

    """comparison on my_optional and my_required.

    Args:
        my_optional (boolean): this has a default value of True).
        my_required (boolean): this could be True or False.

    Returns:
        Str: All Arguments

    Examples:
        >>> defaults (True, True)
        True
        >>> defaults (True, False)
        False

    """
    myself = my_optional is my_required
    return myself
