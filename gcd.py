# gcd of number using recursion

answer = 1


def gcd(n1, n2, d):
    global answer
    if d > ((n2 if n1 > n2 else n1) / 2):
        return answer
    if n1 % d == 0 and n2 % d == 0:
        if d > answer:
            answer = d
    return gcd(n1, n2, d + 1)


print(gcd(24, 16, 2))

