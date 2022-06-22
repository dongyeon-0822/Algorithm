def solution(n,a,b):
    answer = 1
    arr = [x+1 for x in range(n)]
    while True:
        arr1 = []
        for i in range(1,len(arr),2):
            if set([arr[i-1],arr[i]]) == set([a,b]):
                return answer
            elif a in [arr[i-1],arr[i]]:
                arr1.append(a)
            elif b in [arr[i - 1], arr[i]]:
                arr1.append(b)
            else:
                arr1.append(arr[i])
        arr=arr1
        answer+=1

    return answer

solution(8,4,7)