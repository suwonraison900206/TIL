result = []
def find(i, j, d):
    global result
    target = N_lst[i][j]

    for q in range(i, i+d):
        for w in range(j, j+d):

            if N_lst[q][w] != target:

                new_d = d // 2
                result.append('(')
                for ii in range(2):
                    for jj in range(2):

                        find(i + ii * new_d, j + jj *new_d, new_d)
                        # find(i + ii * newd, j + jj * newd, newd)

                result.append(')')

                return

    result.append(str(target))


N = int(input())
N_lst = [list(map(int,input())) for __ in range(N)]
find(0, 0, N)
print(''.join(result))