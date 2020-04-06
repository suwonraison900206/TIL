import sys
sys.stdin = open("1486.txt")

t = int(input())

for test_case in range(t):
    N, B = list(map(int, input().split()))
    temp = list(map(int, input().split()))
    n = len(temp)
    final = []

    for i in range(1, 1 << n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum = sum + temp[j]

        final.append(sum)
    final.sort()
    print(final)


    for i in range(len(final)):
        if final[i] >= B:
            print('#{} {}'.format(test_case+1, final[i] - B))
            break


    # suml = []
    # for i in range(1, 1 << len(tall)):
    #     sum = 0
    #     for j in range(len(tall)):
    #         if i & (1 << j):
    #             sum += tall[j]
    #     suml.append(sum)
    # suml.sort()
    #


    #
    # sum = []
    #
    # for i in range(len(final)):
    #     cnt = 0
    #     for j in range(len(final[i])):
    #         cnt = cnt + final[i][j]
    #
    #     sum.append(cnt)
    #
    #
    # sum_result = []
    #
    # for i in range(len(sum)):
    #     sum_result.append(sum[i] - B)
    #
    #
    # sum_result.sort()
    #
    #
    #
    # final_result = []
    #
    # for i in range(len(sum_result)):
    #     if sum_result[i] >= 0:
    #         final_result.append(sum_result[i])
    #
    # print('#{} {}'.format(test_case+1, final_result[0]))






