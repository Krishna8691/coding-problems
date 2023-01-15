# convert a +ve number from decimal to binary

def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n / 2)) 

print(decimalToBinary(200))

# 8 / 2 = 0
# 4 / 2 = 0
# 2 / 2 = 0
# 1 

# 11 / 2 = 1
# 5 / 2 = 1
# 2 / 2 = 0
# 1
# 1011