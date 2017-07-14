nums = []

def factorial(x):
    if x == 0:
        return 1
    y = x
    for i in range(1, x):
        y *= i
    return y

facts = []

result = 0

for i in range(0, 10):
    facts.append(factorial(i))

for i in range(3, 100000):
    num = 0
    if i % 100000 == 0:
        print(i)
    for digit in str(i):
        num += facts[int(digit)]
    if num == i:
        nums.append(i)
        print(num)
        
result = 0

for num in nums:
    result += num

print(result)
