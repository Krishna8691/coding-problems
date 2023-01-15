# power of a number

def power(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n * power(n, p - 1)

print(power(3, 0))