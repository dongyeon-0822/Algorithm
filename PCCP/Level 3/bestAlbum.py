def solution(genres, plays):
    answer = []
    dic = {}
    for i,(g,p) in enumerate(zip(genres, plays)):
        if g in dic:
            dic[g].append([p,i])
            dic[g][0] += p
        else:
            dic[g] = [p, [p,i]]
    dic = sorted(dic.items(), key=lambda item : item[1][0], reverse=True)
    print(dic)
    for d in dic:
        tmp = sorted(d[1][1:], key=lambda x:(-x[0],x[1]))
        if len(tmp) < 2:
            answer.append(tmp[0][1])
        else:
            answer.extend([tmp[0][1], tmp[1][1]])
    return answer

# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic", "pop", "test"], [500, 600, 150, 800, 2500, 100]))
# print(solution(["classic"], [300]))