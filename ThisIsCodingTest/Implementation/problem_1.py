input_data = input()
row = int(input_data[1])
column = int(input_data[0]) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for s in steps:
    next_row = row + steps[0]
    next_column = column + steps[1]
    if next_row>=1 and next_row<=8 and next_column>= 1 and next_column<=8:
        result += 1
print(result)