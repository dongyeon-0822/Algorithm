def solution(lottos, win_nums):
    answer = []
    znum = 0
    correct = 0
    for i in lottos:
        if i==0:
            znum+=1
        else:
            for j in win_nums:
                if i==j:
                    correct+=1

    max=min=0
    if (correct+znum)<=1:
        max=6
    else:
        max=7-(correct+znum)
    if correct<=1:
        min=6
    else:
        min=7-correct

    answer.append(max)
    answer.append(min)
    return answer