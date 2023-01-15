def isPalindrome(strng):
    if strng[0] != strng[len(strng) - 1]:
        return False
    elif len(strng) in [1, 2]:
        return True
    else: 
        return isPalindrome(strng[1:-1])

print(isPalindrome('amanaplanacanalpandemonium'))
