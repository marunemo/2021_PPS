word = input().upper()
maxCount = 0
for i in set(word):
    count = word.count(i)
    if maxCount < count:
        maxCount = count
        maxWord = i
    elif maxCount == count:
        maxWord = "?"
print(maxWord)