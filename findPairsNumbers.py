# program to find paris of numbers that sum up to a given target

def findPairs(list, target):
    result = []
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                continue
            if list[i] + list[j] == target:
                if [list[i], list[j]] not in result:
                    result.append([list[i], list[j]])
    return result

print(findPairs([1, 2, 3, 2, 3, 4, 5, 6], 6))
                