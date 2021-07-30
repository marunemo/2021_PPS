_,a = input(), list(map(int, input().split()))
sumLog = []
for i in range(len(a)):
    maxSum = 0
    for j in range(i):
        if a[i] < a[j] and sumLog[j] >= maxSum:
            maxSum = sumLog[j]
    sumLog.append(maxSum + a[i])
print(max(sumLog))