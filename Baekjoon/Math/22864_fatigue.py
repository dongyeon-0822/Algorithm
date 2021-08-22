if __name__ == '__main__':
    A,B,C,M = list(map(int,input().split()))
    f = 0
    w = 0
    for i in range(24):
        if f+A <= M:
            w += B
            f += A
        else:
            f -= C
            if f < 0:
                f = 0
    print(w)