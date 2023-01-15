# fibonacci - 1 1 2 3 5 8 13 21 ....
def generateFibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci n number should be +ve & integer num'
    if n in [1, 2]:
        return 1
    else:
        return generateFibonacci(n - 2) + generateFibonacci(n - 1)


print(generateFibonacci(11))