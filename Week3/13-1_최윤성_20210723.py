n,k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
count = 0
for i in money[::-1]:
    if k >= i:
        count += k // i
        k %= i
print(count)