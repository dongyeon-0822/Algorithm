import sys
input = sys.stdin.readline

for i in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    answer = 0
    for idx in range(2, N-2):
        if height[idx-2] < height[idx] and height[idx-1] < height[idx] and height[idx+1] < height[idx] and height[idx+2] < height[idx]:
            view = height[idx] - max(height[idx-2], height[idx-1], height[idx+1], height[idx+2])
            answer += view
    print('#' + str(i+1), answer)