if __name__=='__main__':
    arr = []
    length = []
    for i in range(5):
        arr.append(input())
        length.append(len(arr[-1]))
    for j in range(max(length)):
        for i in arr:
            if len(i)<=j:
                pass
            else:
                print(i[j],end='')