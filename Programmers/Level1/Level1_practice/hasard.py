def solution(x):
    answer = True
    _x=str(x)
    sum=0
    for i in range(len(_x)): sum+=int(_x[i])

    if x%sum==0: answer=True
    else: answer=False
    return answer

if __name__ =='__main__':
    solution(12)