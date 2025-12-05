# 2.1. GCD
# Problem:
# Given two integers a and b, compute their Greatest Common Divisor (GCD) using the Euclidean algorithm.
def gcd_euclidean(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b

    return a


# 2.2. LCM
# Problem:
# Given two integers a and b, find their Least Common Multiple (LCM) using LCM = (a*b) / GCD.
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_euclidean(a, b)