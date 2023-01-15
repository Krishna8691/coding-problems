# Program to find a sub array with a given sum
# Below is the sliding window or the two pointers technique so to say
# This technique is efficient the time complext is O(n)
def findSubArrayWithGivenSum(list, target):
    sum = 0
    start = 0
    end = 0
    n = len(list)
    for i in range(n):
        sum += list[i]
        end = i
        if sum > target:
            while sum > target:
                sum -= list[start]
                start += 1
        if sum == target:
            return start+1, end+1

print(findSubArrayWithGivenSum([1, 4, 20, 3, 10, 5], 33))