from itertools import permutations

def cal(a,b,op):
    if op=='+':
        return int(a)+int(b)
    elif op=='-':
        return int(a)-int(b)
    elif op=='*':
        return int(a)*int(b)

def solution(expression):
    answer = []
    num = []
    op = []
    n = ''
    for e in expression:
        if e.isdigit():
            n+=e
        else:
            num.append(n)
            op.append(e)
            n=''
    for i in permutations(list(set(op)),len(set(op))):
        for j in i:
            index = [idx for idx, x in enumerate(op) if x==j]
            for idx in index:
                num[idx] = cal(num[idx], num[idx+1],j)
                num.pop(idx+1)
                op.pop(idx)
    answer.append(abs(num[0]))
    return max(answer)
