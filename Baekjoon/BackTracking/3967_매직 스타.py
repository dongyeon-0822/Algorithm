# pypy 만 통과
import sys
input = sys.stdin.readline

def check_line(): # 모든 줄의 합이 26인지 확인
    line_1 = sum(ord(magic_star[x][y]) - 64 for x, y in line_list[0])
    line_2 = sum(ord(magic_star[x][y]) - 64 for x, y in line_list[1])
    line_3 = sum(ord(magic_star[x][y]) - 64 for x, y in line_list[2])
    line_4 = sum(ord(magic_star[x][y]) - 64 for x, y in line_list[3])
    line_5 = sum(ord(magic_star[x][y]) - 64 for x, y in line_list[4])
    line_6 = sum(ord(magic_star[x][y]) - 64 for x, y in line_list[5])

    return all(line == 26 for line in [line_1, line_2, line_3, line_4, line_5, line_6])

def check_partial_line(pos):
    for line in line_list:
        if any((x, y) == (empty_x[pos], empty_y[pos]) for x, y in line):
            total_sum = 0
            valid = True
            for x, y in line:
                if magic_star[x][y] == 'x':
                    valid = False
                    break
                total_sum += ord(magic_star[x][y]) - 64
            if valid and total_sum != 26:
                return False
    return True

def solve(pos, best_result):
    # 모든 빈칸 다 채운 경우
    if pos == len(empty_x):
        if check_line():
            current_result = [magic_star[x][y] for x, y in positions]
            return min(best_result, current_result)  # 사전순으로 비교
        return best_result

    # 빈칸에 1부터 12까지의 숫자를 넣기
    for i in range(1, 13):
        if not num_used[i]:
            num_used[i] = True
            magic_star[empty_x[pos]][empty_y[pos]] = chr(64 + i)

            # 가지치기: 채운 상태에서 일부 줄의 합이 26이 되는지 확인
            if check_partial_line(pos):
                best_result = solve(pos + 1, best_result)

            magic_star[empty_x[pos]][empty_y[pos]] = 'x'  # 원상 복구
            num_used[i] = False

    return best_result


num_used = [False] * 13  # 숫자 사용 여부
empty_x, empty_y = [], []  # 빈칸 x, y 좌표
empty_cnt = 0  # 빈칸 개수
positions = [(0, 4),
             (1, 1), (1, 3), (1, 5), (1, 7),
             (2, 2), (2, 6),
             (3, 1), (3, 3), (3, 5), (3, 7),
             (4, 4)]
line_list = [
    [(0, 4), (1, 3), (2, 2), (3, 1)],
    [(3, 1), (3, 3), (3, 5), (3, 7)],
    [(3, 7), (2, 6), (1, 5), (0, 4)],
    [(1, 1), (2, 2), (3, 3), (4, 4)],
    [(4, 4), (3, 5), (2, 6), (1, 7)],
    [(1, 7), (1, 5), (1, 3), (1, 1)]
]

magic_star = [list(input().rstrip()) for _ in range(5)]
for i in range(5):
    for j in range(9):
        if 'A' <= magic_star[i][j] <= 'L':
            num_used[ord(magic_star[i][j]) - 64] = True
        if magic_star[i][j] == 'x':
            empty_x.append(i)
            empty_y.append(j)

answer = solve(0, ['Z'] * 12)

for i, (x, y) in enumerate(positions):
    magic_star[x][y] = answer[i]

for row in magic_star:
    print(''.join(row))