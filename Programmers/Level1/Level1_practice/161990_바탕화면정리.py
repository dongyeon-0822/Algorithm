def solution(wallpaper):
    files = [(i,j) for i in range(len(wallpaper)) for j in range(len(wallpaper[i])) if wallpaper[i][j] == '#']

    x, y = list(zip(*files))
    return [min(x), min(y), max(x)+1, max(y)+1]