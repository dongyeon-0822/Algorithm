from collections import Counter

def solution(weights):
    answer = 0

    dic = Counter(weights)
    ratio = [2/3, 2/4, 3/4]
    for weight in set(weights):
        answer += (dic[weight] * (dic[weight] - 1)) // 2 if dic[weight] >= 2 else 0
        answer += sum([dic[weight] * dic[weight * r] for r in ratio if weight * r in dic])

    return answer

print(solution([100,180,360,100,270]))