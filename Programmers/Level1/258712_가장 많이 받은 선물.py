from collections import Counter, defaultdict
from itertools import combinations

def solution(friends, gifts):
    answer = dict.fromkeys(friends, 0)
    count_dic = dict.fromkeys(friends, 0) # 선물 지수
    gift_dic = Counter(gifts) # 주고 받은 기록
    print(gift_dic)
    for gift in gifts:
        a, b = gift.split()
        count_dic[a] += 1
        count_dic[b] -= 1
    for a, b in list(combinations(friends, 2)):
        x = a + " " + b
        y = b + " " + a
        if gift_dic[x] > gift_dic[y]:
            answer[a] += 1
        elif gift_dic[x] < gift_dic[y]:
            answer[b] += 1
        else:
            if count_dic[a] > count_dic[b]:
                answer[a] += 1
            elif count_dic[a] < count_dic[b]:
                answer[b] += 1

    return max(answer.values())

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))