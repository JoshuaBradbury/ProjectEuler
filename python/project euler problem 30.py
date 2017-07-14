nums = []

for i in range(2, 200000):
    num = 0
    for digit in str(i):
        num += int(digit) ** 5
    if num == i:
        nums.append(i)
        print(num)
        
result = 0

for num in nums:
    result += num

print(result)
