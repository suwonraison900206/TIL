N = int(input())
N_lst = [int(input()) for __ in range(N)]

N_lst.sort(reverse=False)


for i in N_lst:
    print(i)