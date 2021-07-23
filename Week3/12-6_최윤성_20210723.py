a,b,f = 1,1,int(input())
for _ in range(f-1):
    a,b = b,a+b
print(a)