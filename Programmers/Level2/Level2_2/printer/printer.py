def solution(priorities, location):
    answer = 0
    queue=[]
    for i in range(len(priorities)):
        queue.append(i)
    while True:
        _max=max(priorities)
        if priorities[queue[0]]==_max:


    return answer