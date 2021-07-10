case = int(input())
computer = []
for _ in range(case):
    computer.append(input())
for i, word in enumerate(computer):
    print("String #"+str(i + 1))
    print("".join(map(lambda x : chr(ord(x) + 1) if x != "Z" else "A", word)))
    if i != len(computer) - 1:
        print()