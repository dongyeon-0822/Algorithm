def solution(info, query):
    answer = []
    info_list = []
    for i in info:
        info_list.append(i.split())
    # info_list.sort(key=lambda x: x[4])
    for q in query:
        query_list = [x for x in q.split() if x != 'and']
        arr = []
        for i in info_list:
            if i[0]==query_list[0] or query_list[0]=='-':
                if i[1]==query_list[1] or query_list[1]=='-':
                    if i[2] == query_list[2] or query_list[2] == '-':
                        if i[3] == query_list[3] or query_list[3] == '-':
                            if int(i[4])>= int(query_list[4]) or query_list[4] == '-':
                                arr.append(i)
        answer.append(len(arr))

    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])