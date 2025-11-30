"""
1. Prime Numbers
Problem:
    Given an integer n, determine whether it is a prime number.
"""
import math


# approach 1 - brute force
def check_prime_1(n : int) -> bool:
    if n <=1:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# trial division
def check_prime_2(n: int) -> bool:
    if n == 2:
        return True

    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1 , 2):
        if n % i == 0:
            return  False

    return True


# 6k+- 1 optimization
def check_prime_3(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True

        # 2. Check for divisibility by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    print(check_prime_1(7))