n = int(input())
p = list(map(int, input().split()))

for i in range(n):
    maximum = p[i]
    for j in range(i//2+i%2):
        if maximum < p[j] + p[i-j-1]:
            maximum = p[j] + p[i-j-1]
    p[i] = maximum
print(p[n-1])