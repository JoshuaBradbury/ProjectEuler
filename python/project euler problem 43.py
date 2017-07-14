from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

for i in range(1, 10000):
    if i + 3330 < 10000 and i + 6660 < 10000:
        if isPrime(i):
            if isPrime(i + 3330):
                if isPrime(i + 6660):
                    print(i, i + 3330, i + 6660)
