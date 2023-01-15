# Program to rotate a n by n matrix by 90 degreesls
# Method 1 - Using a new seperate list
def rotateMatrix(list):
    result = []
    for i in range(len(list)):
        temp = []
        for j in range(len(list)):
            element = list[len(list) - 1 - j][i]
            temp.append(element)
        result.append(temp);
    return result


# a = rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# for i in a:
#     print(i)


# Method 3 - Inplace swapping with transpose logic
def rotateMatrixInPlace(list):
    # finding transpose of the matrix
    n = len(list)
    for i in range(n):
        for j in range(i, n):
            temp = list[i][j]
            list[i][j] = list[j][i]
            list[j][i] = temp
    first = 0
    last = n - 1
    #  swap elements now
    for i in range(n):
        first = 0
        last = n - 1
        for j in range(n):
            if first == last or first > last:
                continue
            temp = list[i][first]
            list[i][first] = list[i][last]
            list[i][last] = temp
            first = first + 1
            last = last - 1
    return list

# a = rotateMatrixInPlace([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# for i in a:
#     print(i)

#  Method 4 - inplace efficient method
def rotateEfficiently(list):
    n = len(list)
    # outer loop decides no of layers
    for i in range(0, int(n/2)):
        # inner loop rearranges elements in kind of like layers
        for j in range(i, n-1-i):
            # storing top most element
            temp = list[i][j]
            # starting anticlockwise previous bottom element comes to above place
            # bottom left to top left 
            list[i][j] = list[n-j-1][i]
            # previous element comes to above place
            # bottom right to bottom left
            list[n-j-1][i] = list[n-i-1][n-j-1]
            # previous element comes to above place
            # top right to bottom right 
            list[n-i-1][n-j-1] = list[j][n-i-1]
            # temp to top right
            list[j][n-i-1] = temp
    return list

a = rotateEfficiently([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
for i in a:
    print(i)