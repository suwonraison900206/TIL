import sys
import copy
from itertools import combinations
sys.stdin = open('연구소3.txt')

N, M = map(int,input().split())
lst = [list(map(int,input().split())) for __ in range(N)]
virus_lst = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            virus_lst.append((i,j))

k = list(combinations(virus_lst,M))

print(k)
print(k[0][0])
print(k[0])

for i in range(len(k)):
    lst2 = copy.deepcopy(lst)


