
k = []
result = [[]]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def selectionsort(a) :
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            k.append(a[i][j])

    for i in range(0, len(k) - 1):
        min = i
        for j in range(i + 1, len(k)):
            if k[min] > k[j]:
                min = j
        k[i], k[min] = k[min], k[i]

    for i in range(k):






    #
    #
    #         min = j
    #         for k in range(j + 1, len(a[i])):
    #             if a[i][min] > a[i][k]:
    #                 min = k
    #         a[i][j], a[i][min] = a[i][min], a[i][j]
    # return a




        # def selectionsort(a):
        #     for i in range(0, len(a) - 1):
        #         min = i
        #         for j in range(i + 1, len(a)):
        #             if a[min] > a[j]:
        #                 min = j
        #         a[i], a[min] = a[min], a[i]
        #     return a
        #
        # a = [2, 4, 7, 9, 11, 19, 23, 25, 13, 16]
        #
        # print(selectionsort(a))
        #








a =[[9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]]

#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])
#
#




print(selectionsort(a))