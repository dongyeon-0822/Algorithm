N, X = map(int, input().split())
visitor = list(map(int, input().split()))

s, e = 0, X
period_visitor = sum(visitor[:e])
answer = [period_visitor, 1]
while e < N:
    period_visitor -= visitor[s]
    period_visitor += visitor[e]
    s += 1
    e += 1
    if period_visitor > answer[0]:
        answer[0] = period_visitor
        answer[1] = 1
    elif period_visitor == answer[0]:
        answer[1] += 1

if answer[0] == 0:
    print("SAD")
else:
    print(answer[0])
    print(answer[1])