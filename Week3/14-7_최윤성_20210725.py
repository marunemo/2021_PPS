n = int(input())
w = set()
for _ in range(n):
    w.add(input())
for _,i in sorted([(len(d),d) for d in w]):
    print(i)