case = int(input())
axis = []
for _ in range(case):
    axis.append(list(map(int, input().split())))
for i in sorted(axis):
    print(i[0], i[1])