t = int(input())

for test_case in range(t):
    N, M = list(map(int,input().split()))
    sample = list(map(int,input().split()))
    result = []
    for i in range(len(sample)-M+1):
        result.append((sample[i:i+M]))
    final_result = []

    for i in range(len(result)):
        cnt = 0
        for j in range(M):
            cnt = cnt + result[i][j]
        final_result.append(cnt)

    print('#{} {}'.format(test_case+1, max(final_result) - min(final_result)))




# d= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
# a = 10
#
# b = 3
#
# c = []
#
#
# e = []
# result = 0
# f = 0
# result1 = []
# for i in range(a - b +1):
#     c.append(d[i:b+i])
#
# for j in range(0, len(c)):
#     result1.append(result)
#     result = 0
#     for z in range(0, b):
#         result = result + int(c[j][z])
# result1.append(result)
#
# print(max(result1) - (result1[1]))
#
#
# #
# # print(len(c))
# #
# # for j in range(0, len(c)):
# #     print((c[j]))