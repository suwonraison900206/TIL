from collections import Counter

def solution(max_weight, specs, names):
    answer = 1
    weight = dict(specs)  # 이중 배열도 간단하게 딕셔너리로 선언해서 저장할 수 있음
    q = max_weight

    for name in names:
        if q - int(weight[name]) >= 0:
            q = q - int(weight[name])
        else:
            answer += 1
            q = max_weight
            q -= int(weight[name])

    return answer


max_weight = 300
specs = [['toy',70], ['snack', 200]]
names =	['toy', 'snack', 'snack']
solution(max_weight, specs, names)