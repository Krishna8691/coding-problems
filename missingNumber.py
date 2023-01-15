# program to find a missing number from 1 to n

def findMissingNumber(list, n):
    sum1 = (n * (n + 1)) / 2
    sum2 = sum(list)
    return sum1 - sum2

print(findMissingNumber([1, 2, 3, 4, 5, 7, 8, 9, 10], 10))