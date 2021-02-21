def solution(new_id):
    new_id=new_id.lower()
    answer=[]
    for i in new_id:
        if i.isalpha() or i.isdigit() or i=='_' or i=='-' or i=='.':
            if len(answer)!=0 and i=='.' and answer[-1]=='.': continue
            answer.append(i)
    if len(answer)!=0 and answer[0]=='.': answer.pop(0)
    if len(answer)!=0 and answer[-1]=='.': answer.pop()
    if len(answer)==0: answer.append('a')
    if len(answer)>=16:
        while len(answer)>15: answer.pop()
        if answer[-1]=='.':answer.pop()
    if len(answer)<=2:
        while len(answer)<3: answer.append(answer[-1])
    return ''.join(answer)

if __name__ =='__main__':
    print(solution("=.="))