
lis = [1, 2, 2, 4]
w_list = [[0 for _ in range(5)] for _ in range(7)]

a = 1
for i in range(lis[0], lis[2]+1):
    for j in range(lis[1]), lis[3]+1):
        a += lis[i][j]
        w_list.append(a)
print(w_list)





# tc = int(input())
# for t in range(1, tc+1):
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     re_list = [list(map(int, input().split())) for _ in range(10)]
#
#     result1_list = []
#     a_result = 0
#     for i in range(A[0], A[2]+1):
#         for j in range(A[1], A[3]+1):
#             a_result += re_list[i][j]
#             result1 = (re_list[i][j]) * 2
#             result1_list.append(result1)
#             for x in range(len(result1_list)):
#                 if result1_list[x] >= 255:
#                     result1_list[x] = 255
#     result1 = sum(result1_list)
#     result11 = result1 - a_result
#
#
#     result2_list = []
#     b_result = 0
#     for v in range(B[0], B[2]+1):
#         for w in range(B[1], B[3]+1):
#             b_result += re_list[v][w]
#             result2 = int((re_list[v][w]) / 2)
#             result2_list.append(result2)
#             for y in range(len(result2_list)):
#                 if result1_list[y] >= 255:
#                     result1_list[y] = 255
#     result2 = sum(result2_list)
#     result22 = result2 - b_result
#
#     result = result11 + result22