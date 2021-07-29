money = int(input())
count = {1:1, 2:1, 3:2, 4:2, 5:1, 6:2, 7:1}

for i in range(8, money+1):
    minCount = i
    for j in range(1, i):
        if minCount > count[j] + count[i - j]:
            minCount = count[j] + count[i - j]
    count[i] = minCount
print(count[money])