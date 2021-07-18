case = int(input())
custom = dict()
for _ in range(case):
    x = input().split()
    if int(x[0]) in custom:
        custom[int(x[0])].append(x[1])
    else:
        custom[int(x[0])] = [x[1]]
for i in sorted(custom):
    for j in custom[i]:
        print(i,j)