def reverse(n : int) -> int:
    tmp = n
    rev = 0
    while tmp > 0:
        digit   = tmp % 10
        rev     = rev * 10 + digit
        tmp     = int(tmp / 10)
        
    return rev

print(reverse(75568))
