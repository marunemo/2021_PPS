_,l = map(int, input().split())
h = sorted(list(map(int, input().split())))
while h:
    if l < h[0]:
        break
    h.pop(0)
    l+=1
print(l)