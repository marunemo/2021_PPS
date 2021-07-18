num = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}

result = dict()
a,b = map(int,input().split())
for i in range(a, b+1):
    read = "" if i < 10 else num[(i//10)]
    read += num[i%10]
    result[read] = i

for i,r in enumerate(sorted(result)):
    print(result[r], end=" ")
    if i % 10 == 9:
        print()
print()