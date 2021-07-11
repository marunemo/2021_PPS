def solution(number, k):
    answer = '0'
    idx,nidx = -1,0
    lidx = len(number)-k
    while k > 0 and idx != len(answer) and nidx != len(number):
        while k > 0 and idx >= 0 and answer[idx] < number[nidx]:
            idx -= 1
            k -= 1
        idx += 1
        answer = answer[:idx] + number[nidx]
        if k == 0:
            answer += number[nidx+1:]
        nidx += 1
    return answer[:lidx]