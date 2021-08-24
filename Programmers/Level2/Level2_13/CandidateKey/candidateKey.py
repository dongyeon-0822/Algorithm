from itertools import combinations

def solution(relation):
    answer = 0
    col = [i for i in range(len(relation[0]))]
    c = [0 for i in range(len(relation[0]))]
    for j in range(len(relation[0])):
        c[j] = [r[j] for r in relation]
        if len(c[j])==len(set(c[j])):
            answer+=1
            col.remove(j)
    comb = [] # 인덱스의 조합(2 이상)
    comb_key = []
    for i in range(2,len(col)+1):
        comb.extend(list(combinations(col,i)))
    for i in comb:
        arr = [[] for _ in range(len(relation))]
        for j in range(len(i)):
            for k in range(len(arr)):
                arr[k].append(c[i[j]][k])
        arr=[tuple(i) for i in arr]
        if len(arr)==len(set(arr)):
            flag = True
            for ck in comb_key:
                if set(ck).issubset(set(i)):
                    flag=False
                    break
            if flag:
                comb_key.append(i)

    return answer+len(comb_key)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])