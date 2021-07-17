n,k = map(int,input().split())
nk_p = []
p = [i + 1 for i in range(n)]
i = 0
while p:
    i = (i + k - 1) % len(p)
    nk_p.append(str(p.pop(i)))
print("<" + ", ".join(nk_p) + ">")