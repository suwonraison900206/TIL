# m = 4 n = 3 m =y값  n =  x 값


def solution(m, n, puddles):

    print(m,n, puddles)

    map_lst =[[0] * m for __ in range(n)]
    for i in range(len(puddles)):
        map_lst[puddles[i][0] -1][puddles[i][1] -1] = -1
    print(map_lst)

    if map_lst[0][1] != -1:
        map_lst[0][1] = 1
    if map_lst[1][0] != -1:
        map_lst[1][0] = 1
    print(map_lst)

    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 1) or (i == 1 and j ==0):
                pass

            q = w = 0
            if map_lst[i][j-1]:
                if map_lst[i][j-1] != 0:
                    q = map_lst[i][j-1]

            if map_lst[i-1][j]:
                if map_lst[i-1][j] != 0:
                    w = map_lst[i][j-1]

            map_lst[i][j] = q + w

    print(map_lst)










m = 4
n = 3
puddles = [[2,2]]
solution(m,n, puddles)