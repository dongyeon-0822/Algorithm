import sys
input = sys.stdin.readline

grid = [list(map(int, list(input().strip()))) for _ in range(8)]

dominos = {}
for i in range(7):
    for j in range(i, 7):
        dominos[(i, j)] = True

visited = [[False] * 7 for _ in range(8)]

def place_domino(x, y, remaining_dominos):
    if y == 7:
        x += 1
        y = 0
    if x == 8: # 모든 칸 채움
        return 1

    if visited[x][y]:
        return place_domino(x, y + 1, remaining_dominos)

    count = 0
    # 가로로 놓기
    if y < 6 and not visited[x][y + 1]:
        num1, num2 = grid[x][y], grid[x][y + 1]
        if (num1, num2) in remaining_dominos and remaining_dominos[(num1, num2)]:
            visited[x][y] = visited[x][y + 1] = True
            remaining_dominos[(num1, num2)] = False
            count += place_domino(x, y + 2, remaining_dominos)
            visited[x][y] = visited[x][y + 1] = False
            remaining_dominos[(num1, num2)] = True
        elif (num2, num1) in remaining_dominos and remaining_dominos[(num2, num1)]:
            visited[x][y] = visited[x][y + 1] = True
            remaining_dominos[(num2, num1)] = False
            count += place_domino(x, y + 2, remaining_dominos)
            visited[x][y] = visited[x][y + 1] = False
            remaining_dominos[(num2, num1)] = True

    # 세로로 놓기
    if x < 7 and not visited[x + 1][y]:
        num1, num2 = grid[x][y], grid[x + 1][y]
        if (num1, num2) in remaining_dominos and remaining_dominos[(num1, num2)]:
            visited[x][y] = visited[x + 1][y] = True
            remaining_dominos[(num1, num2)] = False
            count += place_domino(x, y + 1, remaining_dominos)
            visited[x][y] = visited[x + 1][y] = False
            remaining_dominos[(num1, num2)] = True
        elif (num2, num1) in remaining_dominos and remaining_dominos[(num2, num1)]:
            visited[x][y] = visited[x + 1][y] = True
            remaining_dominos[(num2, num1)] = False
            count += place_domino(x, y + 1, remaining_dominos)
            visited[x][y] = visited[x + 1][y] = False
            remaining_dominos[(num2, num1)] = True

    return count

print(place_domino(0, 0, dominos))