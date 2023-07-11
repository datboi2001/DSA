"""
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time
as part of the show. If it is possible, return YES, otherwise return NO.
"""


def kangaroo(x1, v1, x2, v2):
    """
    :param x1: distance of kangaroo 1 from starting point
    :param v1: speed of kangaroo 1
    :param x2: distance of kangaroo 2 from starting point
    :param v2: speed of kangaroo 2
    """
    # Write your code here
    # Main idea: If the kangaroos meet, then there exists an integer n such that
    # x1 + n * v1 = x2 + n * v2. This is equivalent to (x1 - x2) = n * (v2 - v1).
    # So n = (x1 - x2) / (v2 - v1). If n is an integer, then the kangaroos meet.
    return 'YES' if v1 > v2 and (x1 - x2) % (v2 - v1) == 0 else 'NO'