t = int(input())

for test_case in range(t):
    a = list(map(int, (input().split())))
    b = list(map(int, (input().split())))
    c = list(map(int, (input().split())))
    sum =0

    d = []
    e = []

    k = []
    result = []
    if len(b) < len(c):
        d = b
        e = c
    else:
        d = c
        e = b


    for i in range(len(e)-len(d)+1):
        k.append(e[i:i+len(d)])
    for i in range(len(k)):
        result.append(sum)
        sum = 0
        for j in range(len(d)):
            sum = sum + ((d[j] * k[i][j]))
    result.append((sum))

    print('#{} {}'.format(test_case + 1, max(result)))