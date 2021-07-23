if __name__ == '__main__':
    n = int(input())
    str = []
    for i in range(n):
        str.append(input())
    for s in str:
        alpha = ''.join(set(s))
        arr = []
        for a in alpha:
            if a==' ': continue
            c = s.count(a)
            if len(arr)==0:
                arr.append((c,a))
            else:
                if arr[-1][0] < c:
                    arr.clear()
                    arr.append((c,a))
                elif arr[-1][0] == c:
                    arr.append((c,a))
        if len(arr)>1:
            print('?')
        else:
            print(arr[0][1])

