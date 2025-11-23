"""

3. Divisibility Rules
Problem:
    Given an integer n and a divisor d, determine whether n is divisible by d without using the % operator.

"""


def is_divisible(n, d):
    if d == 0:
        raise ValueError("Divisor d cannot be zero.")

    quotient = n // d
    remainder = n - (quotient * d)

    return remainder == 0