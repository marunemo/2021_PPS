log = input()
score = []
st = 0
st2 = 0
sp = 0
idx = 0
for phase in range(10):
    if log[idx] == "S":
        get = 10
        score.append(get)
        if st > 0:
            score[len(score)-1] += get
            st -= 1
        if st2 > 0:
            score[len(score)-1] += get
            st2 -= 1
        if sp > 0:
            score[len(score)-1] += get
            sp -= 1
        if phase != 9:
            if st > 0:
                st2 = 2
            else:
                st = 2
        idx += 1
    else:
        for _ in range(2):
            if log[idx] == "P":
                get = 10 - (int(log[idx-1]) if log[idx-1] != "-" else 0)
            elif log[idx] == "-":
                get = 0
            else:
                get = int(log[idx])
            score.append(get)
            if st > 0:
                score[len(score)-1] += get
                st -= 1
            if st2 > 0:
                score[len(score)-1] += get
                st2 -= 1
            if sp > 0:
                score[len(score)-1] += get
                sp -= 1
            if log[idx] == "P" and phase != 9:
                sp = 1
            idx += 1
if log[idx-1] == "S" or log[idx-1] == "P":
    for _ in range(2 if log[idx-1] == "S" else 1):
        if log[idx] == "S":
            get = 10
        elif log[idx] == "P":
            get = 10 - (int(log[idx-1]) if log[idx-1] != "-" else 0)
        elif log[idx] == "-":
            get = 0
        else:
            get = int(log[idx])
        score.append(get)
        if st > 0:
            score[len(score)-1] += get
            st -= 1
        if st2 > 0:
            score[len(score)-1] += get
            st2 -= 1
        if sp > 0:
            score[len(score)-1] += get
            sp -= 1
        idx += 1
print(sum(score))