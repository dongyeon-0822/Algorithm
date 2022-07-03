import sys
input = sys.stdin.readline

N = int(input())
length = 4*N - 3
blank = [2 * n - 1 for n in range(1, N)]
blanks = [(b, length-1-b) for b in blank]
for i in range(length):
    for j in range(length):
        flag = False
        for x in blanks:
            if i in [x[0],x[1]] and j in range(x[0],x[1]+1)\
                or j in [x[0],x[1]] and i in range(x[0],x[1]+1):
                print(' ', end="")
                flag = True
                break
        if not flag:
            print('*', end="")
    print()