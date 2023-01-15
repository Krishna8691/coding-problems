# Write a function to find all pairs of an integer array whose sum is equal to a given number.
# pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']
# Method 1 - using index
def pairSum(myList, sum):
    result = []
    for i in range(len(myList)):
        v = myList[i]
        if sum-v in myList[i:] and myList[i:].index(sum-v):
            result.append(str(v) + ('+' if sum-v > 0 else '-') + str(sum-v))
    return result

# Method 2 - using 2 loops also the problem can be solved
# for method 2 remember the inner loop should start - 
# from i+1 i.e. the next element onwards of the outer loop

print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
