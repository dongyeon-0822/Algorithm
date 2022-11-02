import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

# 시간초과 : 슬라이스를 하는 경우 원소들을 모두 복사하여 새로운 리스트를 만드는 것
# def binary_search(arr, n):
#     middle = len(arr)//2
#     if arr[middle] == n:
#         return True
#     if middle == 0: # 마지막 하나임에도 답이 아닌 경우 False
#         return False
#     elif arr[middle] < n and binary_search(arr[middle:], n):
#         return True
#     elif arr[middle] > n and binary_search(arr[:middle], n):
#         return True
#     return False

def binary_search(arr, start, end, target):
    if start > end:
        return False
    middle = (start+end) // 2
    if arr[middle] == target:
        return True
    elif arr[middle] < target:
        return binary_search(arr, middle+1, end, target)
    elif arr[middle] > target:
        return binary_search(arr, start, middle-1, target)

cards.sort()
for n in nums:
    if binary_search(cards,0,len(cards)-1,n):
        print(1,end=" ")
    else:
        print(0, end=" ")