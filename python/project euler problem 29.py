nums = []

for a in range(2, 101):
    for b in range(2, 101):
        if not (a ** b in nums):
            nums.append(a ** b)

print(len(nums))
