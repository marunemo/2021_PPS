min = eval(input().replace(" ","/"))
con = int(input())
for _ in range(con):
    x,y = map(int,input().split())
    if x/y < min:
        min = x/y
print("%.2f" % (min*1000))