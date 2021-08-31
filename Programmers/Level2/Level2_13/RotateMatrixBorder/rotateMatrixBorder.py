import copy
def solution(rows, columns, queries):
    answer = []
    arr = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    _arr = [a[:] for a in arr]
    for q in queries:
        value = set()
        x1,y1,x2,y2 = [q[0]-1,q[1]-1,q[2]-1,q[3]-1]
        _arr[x1][y1+1:y2+1]=arr[x1][y1:y2]
        value.update(arr[x1][y1:y2])
        _arr[x2][y1:y2]=arr[x2][y1+1:y2+1]
        value.update(arr[x2][y1+1:y2+1])
        for i in range(x1,x2):
            _arr[i+1][y2] = arr[i][y2]
            value.add(arr[i][y2])
        for i in range(x1,x2):
            _arr[i][y1] = arr[i+1][y1]
            value.add(arr[i+1][y1])
        answer.append(min(value))
        arr=[a[:] for a in _arr]

    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])