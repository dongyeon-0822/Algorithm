def solution(cards1, cards2, goal):
    answer = 'Yes'
    idx_1, idx_2 = 0,0
    for g in goal:
        if idx_1 < len(cards1) and cards1[idx_1] == g:
            idx_1 += 1
            continue
        elif idx_2 < len(cards2) and cards2[idx_2] == g:
            idx_2 += 1
            continue
        else:
            answer = 'No'
            break

    return answer