T = int(input())
for test_case in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    b = []
    d = []
    for i in range(N):
        for j in range(i, N):
            if i != j:
                b.append(temp[i] * temp[j])

    for i in range(len(b)):
        c = str(b[i])
        Q = 0
        for j in range(len(c) - 1):
            if len(c) == 1:
                d.append(int(c))
            else:
                if c[j] > c[j + 1]:
                    Q = Q + 1
        if Q == 0:
            d.append(int(c))

    if len(d) == 0 or max(d) == 0:
        print('#{} -1'.format(test_case + 1))
    else:
        print('#{} {}'.format(test_case + 1, max(d)))