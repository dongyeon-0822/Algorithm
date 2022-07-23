# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
def solution(N, stages):
    answer = []
    num = [0] * (N+1)
    for s in stages:
        num[s - 1] += 1
    failure = []
    for i in range(N):
        if sum(num[i:]) == 0:
            failure.append([i + 1, 0])
            continue
        failure.append([i + 1, num[i] / sum(num[i:])])
    failure.sort(key=lambda x:-x[1])
    answer = [x[0] for x in failure]
    return answer