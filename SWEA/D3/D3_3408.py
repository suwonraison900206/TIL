t = int(input())

for test_case in range(t):
    N = int(input())



    cnt = (N * (N+1)) // 2

    cnt1 = (N**2)

    cnt2 = (N*(N+1))

    print('#{} {} {} {}'.format(test_case+1, cnt, cnt1, cnt2))