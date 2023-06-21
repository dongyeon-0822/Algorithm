def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine:
        dic[t] = dic.get(t,0) + 1
    sorted_dic = sorted(dic.items(), key=lambda x:-x[1])
    total = 0
    for key,value in sorted_dic:
        total+=value
        answer+=1
        if total >= k:
            break
    return answer