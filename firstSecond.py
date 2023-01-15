# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.

def firstSecond(givenList):
    l1 = 0
    l2 = 0
    for i in range(len(givenList)):
        if givenList[i] > l1:
            l2 = l1
            l1 = givenList[i]
    return (l1, l2)