from collections import Counter

def solution(v):
    answer = []
    check_x = []
    check_y = []

    for x, y in v:
        check_x.append(x)
        check_y.append(y)

    x = Counter(check_x)
    y = Counter(check_y)

    for key, value in x.items():
        if value == 1:
            answer.append(key)
    for key, value in y.items():
        if value == 1:
            answer.append(key)

    return answer