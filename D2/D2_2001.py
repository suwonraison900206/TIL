T = int(input())
for test_case in range(T):
    N_M = input().split()
    N = int(N_M[0])
    M = int(N_M[1])
    array = []
    for n in range(N):
        array.append(list(map(int, input().split(' '))))
    max = 0
    co_list = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = []
            temp.append(i)
            temp.append(j)
            co_list.append(temp)
    for co in co_list:
        sum1 = 0
        for i in range(co[0], co[0] + M, 1):
            for j in range(co[1], co[1] + M, 1):
                sum1 += array[i][j]
            if max < sum1:
                max = sum1
    print(f'#{test_case + 1} {max}')