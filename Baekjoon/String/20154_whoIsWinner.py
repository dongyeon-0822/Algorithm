if __name__ =='__main__':
    alpha = {'A': 3,'B':2,'C':1,'D':2,'E':3,'F':3,'G':3,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':3,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':2,'X':2,'Y':2,'Z':1 }
    str = input()
    result = [alpha[x] for x in str]
    while True:
        arr = []
        for i,j in enumerate(result):
            if i%2 == 0:
                arr.append(j)
            elif i%2 == 1:
                arr[-1] += j
                if arr[-1] > 10:
                    arr[-1] %= 10
        if len(arr) == 1:
            if arr[0] % 2 == 1:
                print("I'm a winner!")
            else:
                print("You're the winner?")
            break
        else:
            result = arr
