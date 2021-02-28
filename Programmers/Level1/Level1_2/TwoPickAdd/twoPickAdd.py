def solution(numbers):
    answer = []
    arr=[]
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            arr.append(numbers[i]+numbers[j])
    arr1=set(arr)
    answer=list(arr1)
    answer.sort()
    return answer