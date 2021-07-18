def solution(a, b):
    md = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31,
          8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    week = "SUN,MON,TUE,WED,THU,FRI,SAT".split(",")
    date = b
    for i in range(1, a):
        date += md[i]
    answer = week[(date + 4) % 7]
    return answer