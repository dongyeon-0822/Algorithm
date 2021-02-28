def solution(N, stages):
    answer = []
    stage=[0]*(N+1)
    for i in stages:
        stage[i-1]+=1
    failure=[[i,0] for i in range(1,N+1)]
    for i in failure:
        reach=sum(stage[i[0]-1:])
        if reach==0:
            i[1]=0
            continue
        i[1]=stage[i[0]-1]/reach
    failure.sort(key=lambda x:x[1],reverse=True)
    answer=[x[0] for x in failure]
    return answer
if __name__ =='__main__':
    print(solution(5,[2,1,2,4,2,4,3,3]))