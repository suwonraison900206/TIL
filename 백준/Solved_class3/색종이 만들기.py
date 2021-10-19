zero, one = 0, 0

def find(i,j,d):
    global zero, one
    start = N_lst[i][j]

    for q in range(i, i+d):
        for w in range(j, + j+d):

            if N_lst[q][w] != start:

                new_d = d // 2
                for ii in range(2):
                    for jj in range(2):

                        find(i + new_d * ii, j + new_d * jj, new_d)

                return

    if start == 0:
        zero +=1
    elif start == 1:
        one +=1


N = int(input())
N_lst = [list(map(int,input().split())) for __ in range(N)]
find(0,0,N)
print(zero)
print(one)