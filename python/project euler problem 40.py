numberString = ""

count = 1
while len(numberString) < 1000000:
    numberString += str(count)
    count += 1

num1 = int(numberString[0:1])
num2 = int(numberString[9:10])
num3 = int(numberString[99:100])
num4 = int(numberString[999:1000])
num5 = int(numberString[9999:10000])
num6 = int(numberString[99999:100000])
num7 = int(numberString[999999:1000000])

result = num1 * num2 * num3 * num4 * num5 * num6 * num7

print(result)
