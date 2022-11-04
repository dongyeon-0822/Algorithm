import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
visited_1 = [[False] *(len(arr[0])) for _ in range(N)]
visited_2 = [[False] *(len(arr[0])) for _ in range(N)]

normal = 0
redGreen = 0

def normalDFS(color, x, y):
    if x<0 or x>=N or y<0 or y>=len(arr[0]) or visited_1[x][y]:
        return False
    if arr[x][y] == color:
        visited_1[x][y] = True
        normalDFS(color, x - 1, y)
        normalDFS(color, x + 1, y)
        normalDFS(color, x, y - 1)
        normalDFS(color, x, y + 1)
        return True
    return False

def redGreenDFS(color, x, y):
    if x<0 or x>=N or y<0 or y>=len(arr[0]) or visited_2[x][y]:
        return False
    if (arr[x][y]!= 'B' and color != 'B') or (arr[x][y] == color == 'B'):
        visited_2[x][y] = True
        redGreenDFS(color, x - 1, y)
        redGreenDFS(color, x + 1, y)
        redGreenDFS(color, x, y - 1)
        redGreenDFS(color, x, y + 1)
        return True
    return False

for i in range(N):
    for j in range(len(arr[0])):
        if normalDFS(arr[i][j], i,j):
            normal += 1
        if redGreenDFS(arr[i][j], i,j):
            redGreen += 1

print(normal, redGreen)