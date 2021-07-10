case = int(input())
group = 0
for _ in range(case):
    word = input()
    prevWord = ""
    wordLog = []
    isGroup = True
    for wd in word:
        if wd != prevWord:
            if wd in wordLog:
                isGroup = False
                break
            else:
                wordLog.append(wd)
        prevWord = wd
    if isGroup: group += 1
print(group)