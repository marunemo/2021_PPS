import math

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                n = nums[i] + nums[j] + nums[k]
                isprime = True
                for x in range(2, int(math.sqrt(n)) + 1):
                    if n % x == 0:
                        isprime = False
                        break
                if isprime:
                    answer += 1
    return answer