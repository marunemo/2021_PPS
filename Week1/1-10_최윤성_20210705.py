testcase = int(input())
name = []

for i in range(testcase):
    name.append(input()[0])

result = [i for i in set(name) if name.count(i) >= 5]
result.sort()
        
if not result:
    print("PREDAJA")
else:
    print("".join(result))