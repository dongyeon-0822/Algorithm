def solution(s):
    s_lst = list(s)
    for i,a in enumerate(s_lst):
        if i==0 and a!=' ':
            s_lst[i] = a.upper()
        elif i!=0 and a.isalnum() and s_lst[i-1]==' ':
            s_lst[i]=a.upper()
        elif a.isalnum():
            s_lst[i] = a.lower()
    return ''.join(s_lst)
