# program to check if a given list is unique or contains duplicate

def isUnique(list):
    traversedElements = []
    for i in list:
        if i in traversedElements:
            return False
        else:
            traversedElements.append(i)
    return True

# In the above program to keep track of traversed elements, 
# I can also use dictionary so key-values can be accessed in a more optimal way

print(isUnique([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]))