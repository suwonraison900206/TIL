def solution(s):
    answer = 0
    k = []

    for i in s:
        if k and i == k[-1]:
            k.pop()
        else:
            k.append(i)

    return int(k== [])
