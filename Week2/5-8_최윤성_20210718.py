def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        divisor = 0
        for j in range(1, i//2+1):
            if i % j == 0:
                divisor += 2
                if j * j == i:
                    divisor -= 1
        if(i == 1): divisor = 1
        answer += i * (1 if divisor % 2 == 0 else -1)
    return answer