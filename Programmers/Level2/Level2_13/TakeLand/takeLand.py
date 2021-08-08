def solution(land):
    for i, l in enumerate(land):
        if i == 0:
            pass
        else:
            land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
            land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
            land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
            land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
            
    return max(land[len(land)-1])
