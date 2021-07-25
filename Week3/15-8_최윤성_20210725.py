_,p = input(), list(map(int, input().split()))
maxup = 0
isup = False
start = 0
for i in range(1,len(p)):
    if p[i-1] < p[i]:
        if not isup:
            isup = True
            start = p[i-1]
    else :
        if isup:
            length = p[i-1] - start
            if maxup < length:
                maxup = length
            isup = False
if isup:
    length = p[i] - start
    if maxup < length:
        maxup = length
    isup = False
print(maxup)