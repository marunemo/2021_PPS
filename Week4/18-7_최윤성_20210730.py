n = int(input())
time = []
maxCount = 0
next = 0
for _ in range(n):
    time.append(list(map(int, input().split()[::-1])))
for end, start in sorted(time):
    if start >= next:
        next = end
        maxCount += 1
print(maxCount)