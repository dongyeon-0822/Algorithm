from itertools import permutations

def cal(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b

def solution(expression):
    answer = []
    num = []
    op = []
    n = ''
    for e in expression:
        if e.isdigit():
            n+=e
        else:
            num.append(int(n))
            op.append(e)
            n=''
    num.append(int(n))

    for i in permutations(list(set(op)),len(set(op))):
        _num=num.copy()
        _op=op.copy()
        for j in i:
            while _op.count(j)!=0:
                idx=_op.index(j)
                _num[idx] = cal(_num[idx], _num[idx+1],j)
                _num.pop(idx+1)
                _op.pop(idx)
        answer.append(abs(_num[0]))
    return max(answer)

solution("100-200*300-500+20")
