def solution(s):
    count = 0
    zero = 0
    while s!='1':
        count += 1
        zero += s.count('0')
        s = format(s.count('1'),'b')
    return [count,zero]