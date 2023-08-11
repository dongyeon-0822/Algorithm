def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx = 0
        for x in skill_tree:
            if x in skill:
                if skill[idx] == x:
                    idx += 1
                else: break
        else: answer += 1
    return answer