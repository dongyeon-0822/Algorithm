def solution(s):
    queue=[]
    for i in s:
        if len(queue)!=0 and queue[-1]==i:
            queue.pop()
        else:
            queue.append(i)
    if len(queue):
        return 0
    else:
        return 1