x = list(input())
i = 0
while i < len(x) - 1:
    if x[i] == "0" and (x[i-1] in "+-" or i == 0) and x[i+1].isdigit():
        x.pop(i)
        i-=1
    i+=1
print(eval("(" + "".join(x).replace("-",")-(") + ")"))