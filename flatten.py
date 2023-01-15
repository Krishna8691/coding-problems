def flatten(arr):
    result = []
    for a in arr:
        if type(a) == int:
            result.append(a)
        else:
            result.extend(flatten(a))
    return result

print(flatten([1, [2, [3, 4], [[5]]]]))
print(flatten([[1], [2], [3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))