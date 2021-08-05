if __name__=='__main__':
    n= int(input())
    num = n
    count = 0
    while True:
        num = sum(map(int,str(num)))
        if num == n:
            break
        else:
            count += 1
    print(count)