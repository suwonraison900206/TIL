def solution(n, s):
    answer = []
    while n != 0:
        k = s // n
        if k == 0:
            return [-1]
        answer.append(k)
        s = s - k
        n = n - 1

    return answer