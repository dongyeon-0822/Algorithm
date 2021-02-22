def solution(s):
    answer = ''
    index=0
    for i in s:
        if i==' ':
            index=-1
            answer+=' '
        elif index%2==0:
            answer+=i.upper()
        else:
            answer+=i.lower()
        index+=1
    return answer