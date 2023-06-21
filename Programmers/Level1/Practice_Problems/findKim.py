def solution(seoul):
    answer = '김서방은 '
    for i in range(len(seoul)):
        if seoul[i]=='Kim':
             answer+='%d에 있다'%i
    return answer