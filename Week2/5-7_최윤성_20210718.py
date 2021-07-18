croAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0
x = input()
for alpha in croAlpha:
    if alpha in x:
        count += x.count(alpha)
        x = x.replace(alpha, " ")
print(count + len(x.replace(" ", "")))