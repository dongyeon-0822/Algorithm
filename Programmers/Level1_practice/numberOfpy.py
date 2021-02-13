def solution(s):
    answer = True
    p=0
    y=0
    for i in range(len(s)):
        if s[i]=='P' or s[i]=='p': p+=1
        elif s[i]=='Y' or s[i]=='y': y+=1
    if(p==y): answer=True
    else: answer=False
    return answer

if __name__ =='__main__':
    print(solution('Pyy'))