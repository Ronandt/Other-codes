
def sums(x):
    if x < 1:
        return x
    x += sums(x-1)
    return x 

print(sums(10))

def sumOfDigits(n):
    if len(str(n)) == 1:
        return n
    return sumOfDigits(sum([int(x) for x in str(n)]))
    
print(sumOfDigits(123999999999999999999999999999999644))


def palindrome(n):
    if len(n) == 1:
        return True
    elif n[0] == n[-1]:
        x = palindrome(n[1 : -1])
    else:
        return False
    return x 

print(palindrome("racecar"))
    
def exp(a, b):
    if b == 1:
        return a 
    a *= exp(a , b-1)
    return a

print(exp(2, 8))