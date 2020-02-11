import sys
sys.stdin = open("파리.txt")


T = int(input())

for test_case in range(T):

    temp = list(map(int,input().split()))

    a = []

    for i in range(temp[0]):
        k = list(map(int,input().split()))
        a.extend(k)



    print(a)

    #
    # a = list(map(int,input().split()))
    #
    # b = []
    # for i in range(a[0]):
    #     temp = list(map(int,input().split()))
    #
    #     b.append(temp)
    #
    #
    # result = []
    # final_result = 0
    # for j in range(a[0] - a[1] + 1):
    #     for k in range(a[0] - a[1] + 1):
    #         sum = 0
    #         for x in range(j, j +a[1]):
    #             for y in range(k, k + a[1]):
    #
    #                 sum = sum + b[x][y]
    #         result.append(sum)
    # final_result = max(result)
    #
    #
    # print('#{} {}'.format(test_case + 1, final_result))
    #
