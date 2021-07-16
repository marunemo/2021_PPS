from math import log
num = int(input())
twos = log(num,2)
if twos == twos // 1:
    print(num)
else:
    num -= 2**(twos // 1)
    print(2 * int(num))