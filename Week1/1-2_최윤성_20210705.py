def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        able = True
        for i in range(len(skill) - 1, 0, -1):
            index = tree.find(skill[i])
            if index != -1 and i > 0:
                if tree[:index].find(skill[i - 1]) == -1:
                    able = False
                    break
        if able: 
            answer += 1
                
    return answer

if __name__ == "__main__":
    skill = "CBD"
    skill_trees	= ["BACDE", "CBADF", "AECB", "BDA"]	
    solution(skill=skill, skill_trees=skill_trees)