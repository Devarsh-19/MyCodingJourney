"""
4. Factorization
Problem:
    Given a number n, return all of its prime factors in sorted order.
"""

import math


def get_prime_factors(n):
    """
    Returns all prime factors of n in sorted order.
    Time Complexity: O(sqrt(n))
    """
    if n <= 1:
        return []

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)

    return factors
