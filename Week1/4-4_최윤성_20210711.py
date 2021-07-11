case = int(input())
people = []
for i in range(case):
    a,b = int(input()), int(input())
    floor = [f + 1 for f in range(b)]
    for j in range(a):
        temp = floor.copy()
        floor = [sum(temp[:t+1]) for t in range(b)]
    people.append(floor[b - 1])
for i in people:
    print(i)