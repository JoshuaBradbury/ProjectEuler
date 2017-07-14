from math import sqrt

def isPrime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def getRotatedStrings(number):
    nums = [str(number)]
    for i in range(len(str(number)) - 1):
        last = nums[len(nums) - 1]
        nums.append(last[-1:] + last[:len(last)-1])
    results = []
    for num in nums:
        results.append(int(num))
    return results

def isCircularPrime(n):
    for num in getRotatedStrings(n):
        if not isPrime(num):
            return False
    return True

circularPrimes = []

for i in range(2, 1000000):
    if i % 20000 == 0:
        print(i)
    if isCircularPrime(i):
        circularPrimes.append(i)

print("count: " + str(len(circularPrimes)))
print(circularPrimes)
