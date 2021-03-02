import math

def solution(progresses, speeds):
    answer = []
    days=[]
    for (i,j) in zip(progresses,speeds):
        days.append(math.ceil((100-i)/j))
    print(days)
    max=days[0]
    count=0
    for day in days:
        if day>max:
            answer.append(count)
            count=1
            max=day
        else: count+=1
    answer.append(count)
    return answer
if __name__=='__main__':
    print(solution([93, 30, 55],[1, 30, 5]))