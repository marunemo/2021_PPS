caesar = dict()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passwd = alpha[3:] + alpha[:3]
for i in range(26):
    caesar[passwd[i]] = alpha[i]
print("".join(list(map(lambda x: caesar[x], input()))))