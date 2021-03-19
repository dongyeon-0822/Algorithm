def solution(people, limit):
    answer = 0
    people.sort()
    front=0;back=len(people)-1
    while True:
        if people[front]+people[back]<=limit:
            front+=1;back-=1
            answer+=1
        else:
            back-=1
            answer+=1
        if front>back:
            break
    return answer
