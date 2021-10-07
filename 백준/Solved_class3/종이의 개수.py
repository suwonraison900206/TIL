def find(i, j, d):
    global zero, minus, one

    start = number_lst[i][j]

    for q in range(i, i+d):
        for w in range(j, j+d):

            if number_lst[q][w] != start:

                newd = d // 3

                for ii in range(0, 3):
                    for jj in range(0, 3):

                        find(i + ii* newd, j+ jj*newd, newd)

                return
    if start == 0:
        zero += 1
    elif start == 1:
        one += 1
    elif start == -1:
        minus += 1


N = int(input())
number_lst = [list(map(int,input().split())) for __ in range(N)]
zero, minus, one = 0, 0, 0
find(0, 0, N)
print(minus)
print(zero)
print(one)