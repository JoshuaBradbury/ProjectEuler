from math import sqrt

def getFactors(n):
    startFactors = []
    factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            startFactors.append(i)
    for factor in startFactors:
        factors.append(factor)
        factors.append(int(n / factor))
    factors.remove(n)
    return factors

def sumOfFactorsOf(n):
    factors = getFactors(n)
    result = 0
    for factor in factors:
        result += factor
    return result

def getAmicablePair(a):
    b = sumOfFactorsOf(a)
    if sumOfFactorsOf(b) == a:
        return [a, b]
    return []

amicableNumbers = []

for number in range(1, 100000):
    for num in getAmicablePair(number):
        amicableNumbers.append(num)

finalNums = []
for num in amicableNumbers:
    if not num in finalNums:
        finalNums.append(num)

result = 0

for num in finalNums:
    result += num

print(finalNums)

print(result)
