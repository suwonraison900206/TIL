T = int(input())  # 테스트 케이스 받아옴
for test_case in range(T):
    string = []
    max_len = 0
    for i in range(5):
        temp = input()
        if len(temp) > max_len:
            max_len = len(temp)
        string.append(temp)
    answer = ''
    for i in range(max_len):
        for j in range(5):
            if len(string[j]) != 0:
                answer += string[j][0]
                string[j] = string[j][1:]
    print('#{} {}'.format(test_case + 1, answer))



























# T = int(input())
# for i in range(T):
#     n,m = map(int,input().split())
#     fly_list = []
#     for j in range(n):
#         temp = list(map(int,input().split()))
#         fly_list.append(temp)
#     sum_list = []
#     for j in range(n-m+1):
#         for k in range(n-m+1):
#             sum = 0
#             for x in range(j,j+m):
#                 for y in range(k,k+m):
#                     sum += fly_list[x][y]
#             sum_list.append(sum)
#     result = max(sum_list)
#     print("#{0} {1}".format(i+1,result))
# Collapse
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Message cap_hyunwoo