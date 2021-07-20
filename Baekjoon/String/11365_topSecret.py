if __name__ =='__main__':
    arr=[]
    while True:
        arr.append(input())
        if arr[-1]=='END':
            arr.pop(-1)
            break
    for i in arr:
        print(i[::-1])