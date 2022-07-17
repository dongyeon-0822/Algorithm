# 풀이 참고함 https://khu98.tistory.com/228

from collections import deque
import sys
input = sys.stdin.readline

# 변수 선언 및 입력
N = int(input())
coins = []
arr = [[0]*3 for _ in range(3)]
visited = [False] * 512 # 2^9
num = -1

for _ in range(N):
    coin = []
    for _ in range(3):
        tmp = []
        for x in input().split():
            if x == 'H':
               tmp.append('1')
            else:
                tmp.append('0')
        coin.append(tmp)
    coins.append(coin)

def cvt_arr_to_int():
    global num,arr
    tmp_2 = []  # 1차원 형태
    for a in arr:
        tmp_2.extend(a)
    num = int(''.join(tmp_2), 2)
    return num

def cvt_int_to_arr(n):
    global arr
    idx = 0
    n = bin(n)[2:].rjust(9,'0')
    for i in range(3):
        for j in range(3):
            arr[i][j] = n[idx]
            idx += 1

def is_answer():
    sum_one = [sum(map(int,a)) for a in arr]
    sum_one = sum(sum_one)
    if sum_one == 0 or sum_one == 9:
        return True
    return False

# bfs
def bfs():
    global arr, visited, num
    q = deque()
    cnt = 0
    q.append([num, cnt])
    visited[num] = True

    while q:
        n, cnt = q.popleft() # 큐에서 하나를 꺼내고
        cvt_int_to_arr(n) # 숫자를 arr 로 바꾸기
        if is_answer(): # 답이 존재한다면 return
            return cnt
        # 행을 바꾸기
        for i in range(3):
            for j in range(3): # 바꾸기
                arr[i][j] = ('0' if arr[i][j] == '1' else '1')
            tmp_num = cvt_arr_to_int()
            if not visited[tmp_num]:
                visited[tmp_num] = True
                q.append([tmp_num, cnt + 1])
            for j in range(3): # 되돌리기
                arr[i][j] = ('0' if arr[i][j] == '1' else '1')
        # 열을 바꾸기
        for j in range(3):
            for i in range(3): # 바꾸기
                arr[i][j] = ('0' if arr[i][j] == '1' else '1')
            tmp_num = cvt_arr_to_int()
            if not visited[tmp_num]:
                visited[tmp_num] = True
                q.append([tmp_num, cnt + 1])
            for i in range(3): # 되돌리기
                arr[i][j] = ('0' if arr[i][j] == '1' else '1')
        # 대각선을 바꾸기
        diagonal = [[(0,0),(1,1),(2,2)], [(0, 2), (1, 1), (2, 0)]]
        for d in diagonal:
            for i,j in d: # 바꾸기
                arr[i][j] = ('0' if arr[i][j] == '1' else '1')
            tmp_num = cvt_arr_to_int()
            if not visited[tmp_num]:
                visited[tmp_num] = True
                q.append([tmp_num, cnt + 1])
            for i, j in d: # 되돌리기
                arr[i][j] = ('0' if arr[i][j] == '1' else '1')
    return -1


# main
for coin in coins:
    arr = [c[:] for c in coin] # 전역변수 초기화
    visited = [False] * 512  # 전역변수 초기화
    cvt_arr_to_int() # num 초기화
    print(bfs())