"""
Implements the functions for HW0
"""


def funky_sum(a, b, mix):
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def total(n):
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result
