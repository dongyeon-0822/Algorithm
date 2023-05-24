import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
count = 0

def Z(n, x1, y1, x2, y2):
    global count
    if n != 1:
        Z(n-1, x1, y1, (x2-1)//2, (y2-1)//2)
        Z(n-1, x1, (y2+1)//2, (x2-1)//2, y2)
        Z(n-1, (x2+1)//2, y1, x2, (y2-1)//2)
        Z(n-1, (x2+1)//2, (y2+1)//2, x2, y2)
    else:
        for x, y in [(x1,y1), (x1, y2), (x2, y1), (x2, y2)]:
            if x == r and y == c:
                print(count)
            else:
                count+=1
        return

Z(N, 0,0, 2**N-1, 2**N-1)