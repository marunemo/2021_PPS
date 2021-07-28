import sys

sys.setrecursionlimit(20_000)
input = sys.stdin.readline

def postfix(start, end):
    if start > end:
        return

    start_el = l[start] # 반복문 기준으로, 인덱스로 값을 찾아 호출하는 시간 > 인덱스의 값만을 변수에 저장하여 호출하는 시간
    idx = start + 1

    while idx <= end and l[idx] < start_el:
        idx += 1
    
    postfix(start + 1, idx - 1)
    postfix(idx, end)
    print(start_el)

l  = []
try:
    while True:
        node = input()
        l.append(int(node))
except:
    postfix(0, len(l) - 1)