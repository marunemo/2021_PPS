from math import factorial

n,r = int(input()),int(input())
r -= n
n += r - 1
print(factorial(n)//factorial(n-r)//factorial(r))