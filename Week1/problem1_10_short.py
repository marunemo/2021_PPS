t=int(input())
n=[input()[0]for i in range(t)]
r=[i for i in set(n)if n.count(i)>=5]
print("PREDAJA"if not r else"".join(sorted(r)))