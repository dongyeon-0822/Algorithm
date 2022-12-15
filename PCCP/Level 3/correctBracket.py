def solution(s):
    answer = True
    queue = []
    for i in s:
        if len(queue) == 0:
            queue.append(i)
        elif queue[-1]=='(' and i==')':
            queue.pop()
        else:
            queue.append(i)
    if len(queue):
        return False
    else:
        return True

solution('()()')