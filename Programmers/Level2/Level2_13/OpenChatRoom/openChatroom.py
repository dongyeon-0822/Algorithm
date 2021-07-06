def solution(record):
    answer = []
    dic = {}
    l=[]
    for s in record:
        lst=s.split(' ')
        l.append(lst)
        if lst[0]=='Enter':
            dic[lst[1]] = lst[2]
        elif lst[0]=='Change':
            dic[lst[1]] = lst[2]

    for i in l:
        str=""
        if i[0]=='Enter':
            str=dic[i[1]]+'님이 들어왔습니다.'
            answer.append(str)
        elif i[0]=='Leave':
            str = dic[i[1]] + '님이 나갔습니다.'
            answer.append(str)
    return answer