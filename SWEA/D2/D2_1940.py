t = int(input())

for test_case in range(t):
    a = int(input())
    km = 0
    cnt = 0
    for i in range(a):
        N = list(map(int, input().split()))

        if N[0] == 1:
            km = km + N[1]
            cnt = cnt + (1 * km)

        elif N[0] == 2:
            km = km - N[1]
            if km < 0:
                km = 0
            cnt = cnt + (1 * km)
        elif N[0] == 0:
            cnt = cnt + (1 * km)

    print('#{} {}'.format(test_case+1, cnt))


