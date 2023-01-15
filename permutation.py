# program to find permutation

# Method 1 to find factorial using recursion
def findFactorial1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * findFactorial1(n - 1)


# Method 2 to find factorial using normal method
def findFactorial2(n):
    product = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            product = i * product
    return product


def findPermutation1(n, r):
    if n < r or r < 0:
        return 'Please enter such that n >= r >= 0'
    else:
        return findFactorial1(n) / findFactorial1(n - r)

def findPermutation2(n, r):
    if n < r or r < 0:
        return 'Please enter such that n >= r >= 0'
    else:
        return findFactorial2(n) / findFactorial2(n - r)

print(findPermutation1(10, 3), findPermutation2(10, 3))

