# 1. 10 x 10을 만든다
#
# 2. 문제 조건에 맞게 빨강, 파랑도 만든다
#
# 3. for문안에 인덱스가 같으면 빨강을 먼저 넣고 그다음 파랑 입력
#
# 4. 입력후 다시 포문 돌려서 배열값이 0니 아니면 카운트





T = int(input())

for test_case in range(T):

    result = []
    round = int(input())
    test_in = []
    test_in2 = []
    cnt = 0

    #ls = [list(map(int, input().split())) for _ in range(100)] 100 * 100 2중배열


    for i in range(10):
        for j in range(10):
            test_in.append(0)

    for i in range(10):
        test_in2.append(test_in[i * 10:10 + (i * 10)])  # 10 * 10 배열 만들기

    for k in range(round):
        temp = list(map(int, input().split()))

        for i in range(10):
            for j in range(10):
                if i >= temp[0] and i <= temp[2]:
                    if j >= temp[1] and j <= temp[3]:
                        if test_in2[i][j] == 1 or test_in2[i][j] == 2:
                            test_in2[i][j] = 5
                            cnt = cnt + 1
                        else:
                            test_in2[i][j] = temp[4]

    print('#{} {}'.format(test_case + 1, cnt))








































#
#
#     test_in = []
#     test_in2 = []
#
#     red = []
#     red2 = []
#
#     cnt = 0
#
#     for i in range(10):
#         for j in range(10):
#             test_in.append(0)
#
#     for i in range(10):
#         test_in2.append(test_in[i * 10:10 +(i * 10)])
#
#     for i in range(10):
#         for j in range(10):
#             if i > 1 and i < 5:
#                 if j > 1 and j < 5:
#                     test_in2[i][j] = 1
#
#     for i in range(10):
#         for j in range(10):
#             if i > 2 and i < 7:
#                 if j > 2 and j < 7:
#                     if test_in2[i][j] == 1:
#                         cnt = cnt + 1
#                     else:
#                         test_in2[i][j] = 2
#
#     print(cnt)
#
# #
# #
# #
# # for i in range(3):