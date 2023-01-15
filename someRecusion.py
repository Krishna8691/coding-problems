def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr.pop()):
        return True
    else:
        return someRecursive(arr, cb)        

print(someRecursive([1,2,3,4], isOdd))