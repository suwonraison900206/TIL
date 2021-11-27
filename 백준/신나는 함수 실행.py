def reqursion(q, w, e):
    if q <= 0 or w <= 0 or e <= 0:
        return 1
    elif q > 20 or w > 20 or e > 20:
        return reqursion(20, 20, 20)

    if dp[q][w][e] != 0:
        return dp[q][w][e]

    if q < w and w < e:
        dp[q][w][e] = reqursion(q, w, e-1) + reqursion(q, w-1, e-1) - reqursion(q, w-1, e)
        return dp[q][w][e]

    dp[q][w][e] = reqursion(q-1, w, e) + reqursion(q-1, w-1, e) + reqursion(q-1, w, e-1) - reqursion(q-1, w-1, e-1)
    return dp[q][w][e]

max = 21
dp = [[[0] * max for _ in range(max)] for _ in range(max)]
while True:

    a, b, c = map(int,input().split())

    if (a, b, c) == (-1, -1, -1):
        break
    else:
        print('w({}, {}, {}) = {}'.format(a, b, c, reqursion(a,b,c)))


