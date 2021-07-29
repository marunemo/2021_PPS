money = int(input())
count = {0:0, 1:1, 2:1, 3:2, 4:2, 5:1, 6:2, 7:1}

for i in range(8, money+1):
    minCount = i
    if minCount > count[1] + count[i-1]:
        minCount = count[1] + count[i-1]
    if minCount > count[2] + count[i-2]:
        minCount = count[2] + count[i-2]
    if minCount > count[5] + count[i-5]:
        minCount = count[5] + count[i-5]
    if minCount > count[7] + count[i-7]:
        minCount = count[7] + count[i-7]
    count[i] = minCount
print(count[money])