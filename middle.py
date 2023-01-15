# Program to return new list with all elements but the first and last
def middle(list):
    result = []
    for i in range(len(list)):
        if i == 0 or i == len(list) - 1:
            continue
        result.append(list[i])
    return result

print(middle([1, 2, 3, 4]))

# below are other methods we can use but since they are python specific
# we should avoid using them
arr = [1, 2, 3, 4]
print(arr[1:len(arr)-1])
newarr = arr[1:]
del newarr[-1]
print(newarr)