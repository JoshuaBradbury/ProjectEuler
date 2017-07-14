def isPalindromic(string):
    return string == string[::-1]

nums = 0

for i in range(1, 1000000):
    if isPalindromic(str(i)):
        if isPalindromic(str(bin(i))[2:]):
            nums += i

print(nums)
