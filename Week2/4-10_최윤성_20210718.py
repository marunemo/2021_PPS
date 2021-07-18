counts = []
a,b = map(int,input().split())
while a != 0 or b != 0:
    count = 0
    f1, f2 = 1, 2
    while f1 <= b:
        if a <= f1 <= b:
            count += 1
        f1, f2 = f2, f1 + f2
    counts.append(count)
    a,b = map(int,input().split())
print(*counts, sep="\n")