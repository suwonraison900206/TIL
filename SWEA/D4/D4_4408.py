import sys
sys.stdin = open("4408.txt")

t = int(input())

for test_case in range(t):
    a = int(input())
    k = []

    for i in range(a):
        k.append(list(map(int,input().split())))
    final_result = []

    cnt = 0
    count = 1

    arr =[0] * 401

    for i in range(len(k)):
        for j in range(k[i][0], k[i][1]+1):
            arr[j] = arr[j] + 1

    print('#{} {}'.format(test_case+1,max(arr)))

    # while count != 0:
    #     count = 0
    #     for i in range(len(k)):
    #         for j in range(i+1, len(k)):
    #             if len(k) == 1:
    #                 break
    #             elif k[j][0] >= k[i][0] and k[j][0] <= k[i][1]:
    #                 cnt = cnt + 1
    #                 final_result.append(k[j])
    #                 count = 1
    #         print(final_result)
    #         break
    #
    #
    # print('#{} {}'.format(test_case+1,cnt+1))


    # print('#{} {}'.format(test_case+1,cnt + 1))
    #
    # stack = 0
    #
    # for i in range(len(final_result)):
    #     for j in range(i+1, len(final_result)):
    #         if final_result[i] == final_result[j]:
    #             stack = stack + 1
    # #
    #
    #
    # if stack == 0 and len(final_result) == 0:
    #     print('#{} {}'.format(test_case+1, 1))
    # elif stack == 0:
    #     print('#{} {}'.format(test_case + 1, 2))
    # elif stack != 0:
    #     print('#{} {}'.format(test_case + 1, stack+2))
