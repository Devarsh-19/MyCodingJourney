"""
1. Prime Numbers
Problem:
    Given an integer n, determine whether it is a prime number.
    Return "YES" if prime, otherwise "NO".
"""

# approach 1 - brute force

def check_prime(n : int) -> False:
    if n <=1:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return False


