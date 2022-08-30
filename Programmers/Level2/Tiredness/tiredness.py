from itertools import permutations
def solution(k, dungeons):
    answer = []
    perm = list(permutations(range(len(dungeons))))
    for p in perm:
        value = k
        cnt = 0
        for i in p:
            if dungeons[i][0] <= value:
                cnt += 1
                value -= dungeons[i][1]
        if cnt == len(dungeons):
            return cnt
        answer.append(cnt)
    return max(answer)

solution(80, [[80, 20], [50, 40], [30, 10]])