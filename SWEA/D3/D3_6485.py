import sys
sys.stdin = open("6485.txt")
t = int(input())
for test_case in range(t):
    N = int(input())
    k = []

    for i in range(N):
        k.append(list(map(int, input().split())))
    C = [0] * 5001

    for i in range(N):
        for j in range(k[i][0], k[i][1]+1):
            C[j] = C[j] + 1

    P = int(input())
    result = []

    for i in range(P):
        number = int(input())
        result.append(C[number])

    final_result = ' '.join(map(str, result))

    print('#{} {}'.format(test_case+1, final_result))


# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     N_list = []
#     for _ in range(N):
#         N_list.append(list(map(int, input().split())))
#     P = int(input())
#     result_list = []
#     for _ in range(P):
#         num = int(input())
#         cnt = 0
#         for i in range(N):
#             for x in range(N_list[i][0], N_list[i][1]+1):
#                 if num == x:
#                     cnt += 1
#         result_list.append(cnt)
#     result = ' '.join(map(str, result_list))
#     print('#{} {}'.format(t, result))
#
