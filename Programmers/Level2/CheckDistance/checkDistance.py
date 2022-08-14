# 약간의 팁을 보고 풀이

def check_O(i,j,arr):
    cnt = 0
    if 0 <= i-1 < 5 and arr[i-1][j] == 'P':
        cnt += 1
    if 0 <= j-1 < 5 and arr[i][j-1] == 'P':
        cnt += 1
    if 0 <= i+1 < 5 and arr[i+1][j] == 'P':
        cnt += 1
    if 0 <= j+1 < 5 and arr[i][j+1] == 'P':
        cnt += 1
    if cnt >= 2:
        return False
    return True

def check_P(i,j,arr):
    cnt = 0
    if 0 <= i-1 < 5 and arr[i-1][j] == 'P':
        cnt += 1
    if 0 <= j-1 < 5 and arr[i][j-1] == 'P':
        cnt += 1
    if 0 <= i+1 < 5 and arr[i+1][j] == 'P':
        cnt += 1
    if 0 <= j+1 < 5 and arr[i][j+1] == 'P':
        cnt += 1
    if cnt >= 1:
        return False
    return True

def check_place(arr):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'O':
                if not check_O(i,j,arr):
                    return False
            if arr[i][j] == 'P':
                if not check_P(i,j,arr):
                    return False
    return True
def solution(places):
    answer = []
    for place in places:
        if not check_place(place):
            answer.append(0)
        else:
            answer.append(1)
    return answer