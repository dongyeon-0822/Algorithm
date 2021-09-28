# 시간초과 미해결
from itertools import combinations

def solution(enter, leave):
    answer = [0]*len(enter)
    result = []
    room = []
    idx_e = 0
    idx_l = 0
    while idx_l<len(leave):
        if len(room)==0:
            room.append(enter[idx_e])
            idx_e+=1
        else:
            if leave[idx_l] in room:
                room.remove(leave[idx_l])
                idx_l+=1
            else:
                room.append(enter[idx_e])
                idx_e += 1
                if len(room) >= 2:
                    # for r in room:
                    #     answer[r-1]+=1
                    for i in list(combinations(room,2)):
                        if list(i) not in result:
                            result.append(list(i))
    for i in result:
        for j in i:
            answer[j-1]+=1
    return answer

print(solution([1,4,2,3], [2,1,3,4]))