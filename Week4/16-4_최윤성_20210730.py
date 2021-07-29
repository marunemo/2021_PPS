from math import factorial

def solution(n):
    answer = 0
    for i in range(n//2+n%2, n+1):
        twoCount = n - i
        answer += factorial(i)//factorial(twoCount)//factorial(abs(i-twoCount))
    return answer % 1234567