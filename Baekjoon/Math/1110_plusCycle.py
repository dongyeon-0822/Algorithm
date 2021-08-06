if __name__=='__main__':
    n = int(input())
    num = n
    count = 0
    while True:
        a = n%10
        b = sum(map(int,str(n)))%10
        n = a*10+b
        count += 1
        if n == num:
            break
    print(count)