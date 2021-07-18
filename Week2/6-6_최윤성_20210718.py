from functools import cmp_to_key
def comp(a,b):
    if len(a) == len(b):
        sa = "+".join(filter(lambda x :x.isdigit(), a))
        sa = 0 if sa == "" else eval(sa)
        sb = "+".join(filter(lambda x :x.isdigit(), b))
        sb = 0 if sb == "" else eval(sb)
        if sa == sb:
            return 1 if a > b else 0 if a == b else -1
        return sa - sb
    return len(a) - len(b)
n = []
for _ in range(int(input())):
    n.append(input())
print(*sorted(n, key=cmp_to_key(comp)),sep="\n")