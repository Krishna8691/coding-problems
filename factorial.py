def factorial(n):
    assert n >= 0, "Please enter positive integer only!"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))