def solution(priorities, location):
    answer = 0
    queue=[]
    for i in range(len(priorities)):
        queue.append(i)
    while True:
        _max=max(priorities)
        if priorities[0]==_max:
            answer+=1
            if queue[0]==location:
                return answer
            del priorities[0]
            del queue[0]
        else:
            priorities.append(priorities[0])
            queue.append(queue[0])
            del priorities[0]
            del queue[0]