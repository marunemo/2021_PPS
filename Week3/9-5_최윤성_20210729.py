import sys

sys.setrecursionlimit(20000)

def delSection(x, y, c):
    grid[x][y] = "0"
    if x != case - 1:
        if grid[x+1][y] == c:
            delSection(x+1,y,c)
    if x != 0:
        if grid[x-1][y] == c:
            delSection(x-1,y,c)
    if y != case - 1:
        if grid[x][y+1] == c:
            delSection(x,y+1,c)
    if y != 0:
        if grid[x][y-1] == c:
            delSection(x,y-1,c)

def delRGsection(x, y, c):
    RGgrid[x][y] = "0"
    if x != case - 1:
        if RGgrid[x+1][y] == c:
            delRGsection(x+1,y,c)
    if x != 0:
        if RGgrid[x-1][y] == c:
            delRGsection(x-1,y,c)
    if y != case - 1:
        if RGgrid[x][y+1] == c:
            delRGsection(x,y+1,c)
    if y != 0:
        if RGgrid[x][y-1] == c:
            delRGsection(x,y-1,c)

case = int(input())
grid = []
RGgrid = []
section = 0
RGsection = 0
for _ in range(case):
    row = input().replace("B","3").replace("R","1")
    grid.append(list(row.replace("G","2")))
    RGgrid.append(list(row.replace("G","1")))
for i in range(case):
    for j in range(case):
        if grid[i][j] != "0":
            section += 1
            delSection(i, j, grid[i][j])
        if RGgrid[i][j] != "0":
            RGsection += 1
            delRGsection(i, j, RGgrid[i][j])
print(section, RGsection)