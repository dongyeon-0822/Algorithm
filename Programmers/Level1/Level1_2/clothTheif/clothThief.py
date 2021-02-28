def solution(n, lost, reserve):
    answer = 0
    lost_=set(lost)-set(reserve)
    reserve_=set(reserve)-set(lost)
    for i in reserve_:
        if i-1 in lost_: lost_.remove(i-1)
        elif i+1 in lost_:lost_.remove(i+1)
    answer=n-len(lost_)
    return answer

if __name__ =='__main__':
    print(solution(5,[2,4],[1,3,5]))