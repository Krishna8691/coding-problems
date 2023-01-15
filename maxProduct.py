# find maximum product of two numbers in given list also can find the pairs itself
def maxProduct(list):
    product = 0
    idx = 0
    for i in range(len(list) - 1):
        if list[idx] * list[i+1] > product:
            product = list[idx] * list[i+1]
            if list[idx] < list[i+1]:
                idx = i + 1
    return product

# other method is using two for loops


# print(maxProduct([11, 1, 2, 3, 4, 23, 44, 65, 47, 87, 43, 2, 3, 0, 8]))
print(maxProduct([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]))