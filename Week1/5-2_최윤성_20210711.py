case = int(input())
result = []
for i in range(case):
    fomula = input().split()
    test = float(fomula[0])
    for t in fomula[1:]:
        if t == "@":
            test *= 3
        elif t == "%":
            test += 5
        elif t == "#":
            test -= 7
    result.append("%.2f" % test)
for i in result:
    print(i)