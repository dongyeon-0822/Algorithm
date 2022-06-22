def solution(str1, str2):
    answer = 0
    s1=[]
    s2=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i:i+2].upper())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s2.append(str2[i:i+2].upper())
    if len(s1)==0 and len(s2)==0:
        return 1*65536

    inter = sum([min(s1.count(i),s2.count(i)) for i in list(set(s1)&set(s2))])
    union = sum([max(s1.count(i), s2.count(i)) for i in list(set(s1) | set(s2))])

    return int((inter/union)*65536)

solution('aa1+aa2','AAAA12')