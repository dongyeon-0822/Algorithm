from itertools import permutations

def cal(a,b,op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b

def solution(expression):
    answer = []

    nums = []
    operators = []
    num = ''
    for e in expression:
        if e.isdigit():
            num += e
        else:
            nums.append(int(num))
            operators.append(e)
            num = ''
    nums.append(int(num))

    for order_operators in permutations(list(set(operators)),len(set(operators))):
        num = nums[:]
        operator = operators[:]
        for op in order_operators:
            while (idx := ''.join(operator).find(op)) != -1:
                num[idx] = cal(num[idx], num[idx + 1], op)
                num.pop(idx + 1)
                operator.pop(idx)
        answer.append(abs(num[0]))
    return max(answer)

solution("100-200*300-500+20")