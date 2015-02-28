#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some pretty crazy math."""


import hamlet

def crazy_math(4, 100000, 8, 98):
    """This function does crazy math using facts from hamlet file.

    Args:
        monkeys (int): Number of monkeys available.
        hours (mixed): Number of hours available to produce Hamlet.
        typewriters (int): Number of available typewriters (Optional).
        bananas (int): Number of available bananas
        POSITIONING (int): calculates the crazy math

    Returns:
        float: The percentage likelihood of producing Hamlet as a float.

    Examples:

        >>>
    """
    banana_effect = bananas * BANANA_MULTIFIER
    utilization = monkeys / SHIFTS

    POSITIONING = (hours * (utilization + banana_effect)) / HAMLETHOURS

    return POSITIONING 
