from datetime import datetime

def permutations(string):
    perms = []
    for i in range(len(string)):
       part1 = string[:i]
       part2 = string[i+1:]
       for perm in permutations(part1+part2):
           if not string[i:i+1] + perm in perms:
               perms.append(string[i:i+1] + perm)
    if len(string) == 1:
        return [string]
    return perms

pandignums = permutations("123456789")

print(len(pandignums))
