# sum of digits of a +ve integer eg - 1234 = 1+2+3+4

def sumOfDigits1(n):
    numberStr = str(n)
    length = len(numberStr)
    firstDigit = int(numberStr[0])
    remainingDigits = n - firstDigit * (10**(length-1))
    if length == 1:
        return n
    else:
        return firstDigit + sumOfDigits1(remainingDigits)

def sumOfDigits2(n):
    if (n % 10 == n):
        return n
    else:
        return n % 10 + sumOfDigits2(int(n / 10))

print(sumOfDigits2(12345))