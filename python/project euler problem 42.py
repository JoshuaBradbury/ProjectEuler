f = open("project euler problem 42 - words.txt", "r")

line = f.readline()
words = line.replace("\"", "").lower().split(",")

f.close()

triangleNumbers = []

for i in range(1, 50):
    triangleNumbers.append(int(0.5 * i * (i + 1)))

def getWordValue(word):
    value = 0
    for letter in word:
        value += "abcdefghijklmnopqrstuvwxyz".find(letter) + 1
    return value

triangleWords = 0

for word in words:
    if getWordValue(word) in triangleNumbers:
        triangleWords += 1

print(triangleWords)
