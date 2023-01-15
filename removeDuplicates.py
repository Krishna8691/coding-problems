# program to remove/find duplicates from a list
# method 1
def removeDuplicates(myList):
    result = []
    duplicate = []
    for i in range(len(myList)):
        if myList[i] in result:
            duplicate.append(myList[i])
            continue
        result.append(myList[i])
    # return duplicate if you have to find the duplicates
    # return duplicate if len(duplicate) > 0 else None 
    return result

# method 2
def removeDuplicates(myList):
    result = []
    duplicate = []
    for i in myList:
        if i in result:
            duplicate.append(i)
            continue
        result.append(i)
    # return duplicate if you have to find the duplicates
    # return duplicate if len(duplicate) > 0 else None 
    return result