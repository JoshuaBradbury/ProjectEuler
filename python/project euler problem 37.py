from math import sqrt

def getNums(num):
    nums = []
    for i in range(len(num)):
        nums.append(num[i:])
        nums.append(num[:i])
    nums.remove("")
    return nums

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

for i in range(10, 1000000):
    lst = getNums(str(i))
    truncatablePrimes = True
    for num in lst:
        if not isPrime(int(num)):
            truncatablePrimes = False
            break
    if truncatablePrimes:
        print(i, lst)
