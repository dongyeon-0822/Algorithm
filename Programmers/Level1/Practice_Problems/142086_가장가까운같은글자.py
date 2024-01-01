from collections import defaultdict

def solution(s):
    answer = []
    dic = defaultdict(int)
    for i, x in enumerate(s,1):
        if dic[x] == 0:
            answer.append(-1)
        else:
            answer.append(i-dic[x])
        dic[x] = i
    return answer