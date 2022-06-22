def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        available=True
        count=0
        for j in i:
            if j in skill:
                if skill[count]==j:
                    count+=1
                else: available=False
        if available: answer+=1
    return answer