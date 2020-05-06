import sys
import copy
from itertools import permutations , combinations

sys.stdin = open('chicken.txt')

N , M = map(int,input().split())

map_lst = [list(map(int,input().split())) for __ in range(N)]
chicken_lst = []

sum_lst = []


lst_1 = []

for i in range(N):
    for j in range(N):
        if map_lst[i][j] == 2:
            map_lst[i][j] = 0
            chicken_lst.append((i,j))
        elif map_lst[i][j] == 1:
            lst_1.append((i,j))


k = list(combinations(chicken_lst,M))

Q = (0, 0)
lst = []
for i in range(len(k)):
    lst2 = copy.deepcopy(map_lst)
    final_lst = []
    for j in range(M):
        lst2[k[i][j][0]][k[i][j][1]] = 2


    for j in range(len(lst_1)):
        for q in range(M):
            lst.append(abs(lst_1[j][0] - k[i][q][0]) + abs(lst_1[j][1] - k[i][q][1]))

        final_lst.append(min(lst))
        lst = []

    sum_lst.append((sum(final_lst)))

result_lst = []
final_lst = []

print(min(sum_lst))


