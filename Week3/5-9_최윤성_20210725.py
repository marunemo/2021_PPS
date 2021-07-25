def solution(dirs):
    answer = 0
    grid = dict()
    pos = [0,0]
    for i in range(-5, 6):
        for j in range(-5, 6):
            grid[i,j] = ""
    for i in dirs:
        x,y = pos[0],pos[1]
        if i == "U" and pos[1] < 5:
            pos[1] += 1
        elif i == "R" and pos[0] < 5:
            pos[0] += 1
        elif i == "D" and pos[1] > -5:
            pos[1] -= 1
        elif i == "L" and pos [0] > -5:
            pos[0] -= 1
        if pos[0] != x or pos[1] != y:
            if i not in grid[x,y]:
                grid[x, y] += i
                if i == "L":
                    grid[pos[0], pos[1]] += "R"
                elif i == "R":
                    grid[pos[0], pos[1]] += "L"
                elif i == "U":
                    grid[pos[0], pos[1]] += "D"
                elif i == "D":
                    grid[pos[0], pos[1]] += "U"
                answer += 1
        print(pos)
    return answer