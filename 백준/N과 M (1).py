from itertools import combinations, permutations

N, M = map(int,input().split())

n_lst = [i for i in range(1, N+1)]
for i in permutations(n_lst, M):

    for j in i:
        print(j, end =' ')
    print()