import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
for i, b in enumerate(blocks):
    if b > H:
        blocks[i] = H

rain = 0
max_height, min_height = 0, H
depth = []
for block in blocks:
    if max_height <= block:
        if max_height - min_height > 0:
            rain += sum([max_height - d for d in depth])
        max_height, min_height = block, H # 웅덩이 초기화
        depth = []
    elif min_height < block < max_height:
        for i, d in enumerate(depth):
            if block - d > 0:
                rain += block - d
                depth[i] = block
        depth.append(block)
        min_height = block
    elif block <= min_height:
        depth.append(block)
        min_height = block
print(rain)

# 4 8
# 2 1 1 4 3 2 1 3