"""
Implements the functions for HW0
"""


def funky_sum(a, b, mix):
    """
    :param a: the first number
    :param b: the second number
    :param mix: control the return value
    :return: if mix is less or equal to 0, return a; if mix is larger or
            equal to 1, return b; if mix is between 0 and 1 (exclusively),
            return the sum if 1-mix times a and mix times b
            (linear interpolation).
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def total(n):
    """
    :param n: number use to be the uppper bound of adding value
    :return: if n is negative, return None value; if not, return
            the sum of all integers from 0 to n (inclusively).
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source, c1, c2):
    """
    :param source: the target string to be processed
    :param c1: the first swapping character
    :param c2: the second swapping character
    :return: a copy of source with all occurrences of c1 and c2 swapped
    """
    result = ''
    for i in source:
        if i == c1:
            result += c2
        elif i == c2:
            result += c1
        else:
            result += i
    return result
