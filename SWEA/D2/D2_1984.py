# t = int(input())
#
# for test_case in range(t):
#
#
#
#     a = list(map(int, input().split(' ')))
#     #
#     # for i in range(len(a)-1, 0, -1):
#     #     for j in range(0, i):
#     #         if a[j] > a[j+1]:
#     #             a[j], a[j+1] = a[j+1], a[j]
#
#
#
#     sum = 0
#     result =0
#
#     for i in range(len(a)):
#         sum = sum + a[i]
#
#     result = round((sum - max(a) -min(a)) / 8)
#
#
#
#     print('#{} {}'.format(test_case + 1, result))






T = int(input())
for i in range(T):
    s = 0
    N = list(map(int, input().split()))
    N.sort()
    s = int(sum(N[1:len(N)-1]))
    result = round(s/(len(N)-2))
    print(f'#{i+1} {result}')

