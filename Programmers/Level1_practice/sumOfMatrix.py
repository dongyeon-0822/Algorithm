def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        arr=[]
        for j in range(len(arr1[0])):
            arr.append(arr1[i][j]+arr2[i][j])
        answer.append(arr)
    return answer

if __name__ =='__main__':
    print(solution([[1,2],[2,3]],[[3,4],[5,6]]))