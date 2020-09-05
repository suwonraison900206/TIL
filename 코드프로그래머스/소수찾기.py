def solution(n):
    d = [1] * (n+1)
    d[2] = 1
    d[1] = 0
    d[0] = 0
    for i in range(2, n+1):
        if d[i] != 0:
            k = i
            while k + i <= n:
                k = k + i
                d[k] = 0


    answer = sum(d)
    print(answer)
    return answer


n = 10
solution(n)