def solution(answers):
    answer = []
    stu1=[1,2,3,4,5]
    stu2=[2,1,2,3,2,4,2,5]
    stu3=[3,3,1,1,2,2,4,4,5,5]
    cnt=[0]*3

    for i in range(len(answers)):
        if answers[i]==stu1[i%len(stu1)]:
            cnt[0]+=1
        if answers[i]==stu2[i%len(stu2)]:
            cnt[1]+=1
        if answers[i]==stu3[i%len(stu3)]:
            cnt[2]+=1

    max_cnt=max(cnt)
    for i in range(len(cnt)):
        if cnt[i]==max_cnt:
            answer.append(i+1)
    return answer

if __name__=='__main__':
    print(solution([1,2,3,4,5]))