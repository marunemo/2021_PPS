_,n = input(),list(map(lambda x : x == "A", input()))[::-1]
count = 0
reverse = False
l = len(n)
for i in range(len(n)):
    if i != 0 and n[i] == n[i-1]:
        continue
    if not n[i] ^ reverse:
        count += 1
        if i != l - 1 and not n[i + 1] ^ reverse:
            reverse = not reverse
print(count)