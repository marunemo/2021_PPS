dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
s = sum(dwarf) - 100
for i in range(8):
    if s - dwarf[i] in dwarf:
        dwarf.remove(s-dwarf[i])
        dwarf.remove(dwarf[i])
        break
print(*dwarf,sep="\n")