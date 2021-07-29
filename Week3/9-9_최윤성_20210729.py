target = int(input())
shell = 1
roomRange = 1
while target > roomRange:
    roomRange += shell * 6
    shell += 1
print(shell)