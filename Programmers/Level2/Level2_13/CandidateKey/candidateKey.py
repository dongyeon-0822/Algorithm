from itertools import combinations

def solution(relation):
    answer = 0
    key = [i for i in range(len(relation[0]))]
    c = [0 for i in range(len(relation[0]))]
    for j in range(len(relation[0])):
        c[j] = [r[j] for r in relation]
        if len(c[j])==len(set(c[j])):
            answer+=1
            key.remove(j)
    # 인덱스가 아닌 것끼리 2부터 조합 구해서 튜플로 만들어서 중복 체크!
    com = []
    for i in range(2,len(key)+1):
        com.extend(list(combinations(key,i)))
    for c in com:
        []

    return answer