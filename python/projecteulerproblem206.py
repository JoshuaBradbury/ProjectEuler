from math import sqrt
for i in range(1385024891, 10000000000, 1):
    x = i ** 2
    y = str(int(x))[::2]
    if "12345678" in y[0:8]:
        print(i, y)
    if y == "1234567890":
        print(i)
        break
