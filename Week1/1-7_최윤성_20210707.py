grid = list(map(int,input().split()))

window = []
style = [0 for i in range(5)]

for i in range(5 * grid[0] + 1):
    frame = input()
    if frame.count("#") == grid[1] + 1:
        window.append(frame.replace("#", "").replace("....", ".").replace("****", "*"))

for i in range(grid[0]):
    for shutter in range(4):
        for j in range(grid[1]):
            if (shutter == 0 or window[shutter + 4 * i - 1][j] == "*") and window[shutter + 4 * i][j] == ".":
                style[shutter] += 1
    for j in range(grid[1]):
        if window[shutter + 4 * i][j] == "*":
            style[4] += 1

print(style[0],style[1],style[2],style[3],style[4])