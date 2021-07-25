n,m = map(int, input().split())
dj = []
dbj = []
for _ in range(n):
    dj.append(input())
for _ in range(m):
    bj = input()
    if bj in dj:
        dbj.append(bj)
print(len(dbj))
print(*sorted(dbj), sep="\n")