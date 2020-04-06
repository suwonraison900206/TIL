# arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
#
# n = len(arr)
#
# k = []
#
#
# sum =0
#
#
# for i in range(1<<n):
#     c = []
#     for j in range(n):
#         if i & (1<<j):
#             c.append(arr[j])
#
#     print(c)
#
#
#     # for k in range(1<<n):
#     #     if sum(c[k]) == 0:
#     #         print(True)
#     #     else:
#     #         print(False)
#     #
#

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
cnt = 0

for i in range(1, 1<<len(arr)):

    for j in range(len(arr)):
        if i & (1<< j ):
            sum = sum + arr[j]

    if sum == 0:
        cnt += 1
        print("%d : " % cnt, end='')
        for j in range(len(arr)):
            if i & (1 << j):
                print((arr[j]), end='')
        print()