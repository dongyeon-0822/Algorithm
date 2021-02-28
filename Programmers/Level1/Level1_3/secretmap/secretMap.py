def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        str1=format(i,'b').zfill(n)
        str2=format(j,'b').zfill(n)
        s=''
        for s1,s2 in zip(str1,str2):
            if s1=='1' or s2=='1':
                s+='#'
            else: s+=' '
        answer.append(s)
    return answer
if __name__ == '__main__':
    print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))