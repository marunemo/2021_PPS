_,p = input(), list(map(int, input().split()))
time = 0
stack = 0
for i in sorted(p):
    stack += i
    time += stack
print(time)