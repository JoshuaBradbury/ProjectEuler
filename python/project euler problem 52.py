from itertools import permutations

for i in range(1, 1000000):
    if i % 10000 == 0:
        print(i)
    if "0" in str(i):
        continue
    if int(str(i)[0:2]) < 18:
        perms = set(["".join(p) for p in permutations(str(i))])
        if str(i * 2) in perms:
            if str(i * 3) in perms:
                if str(i * 4) in perms:
                    if str(i * 5) in perms:
                        if str(i * 6) in perms:
                            print("Answer: ", i)
                            break
