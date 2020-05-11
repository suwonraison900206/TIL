from itertools import combinations
import sys
import copy
sys.stdin = open('연구.txt')

N, M = map(int,input().split())
lst = [list(map(int,input().split())) for __ in range(N)]
dx =[-1, 0, 1, 0]
dy =[0, 1, 0, -1]

result = []
zero_lst = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            zero_lst.append((i,j))

zero_lst2 = list(combinations(zero_lst,3))

print(zero_lst2)

for i in range(len(zero_lst2)):
    lst2 = copy.deepcopy(lst)
    virus_lst = []
    for j in range(3):
        lst2[zero_lst2[i][j][0]][zero_lst2[i][j][1]] = 1
    for q in range(N):
        for w in range(M):
            if lst[q][w] == 2:
                virus_lst.append((q, w))

    while virus_lst:
        k = virus_lst.pop(0)
        for z in range(4):
            di = k[0] + dx[z]
            dj = k[1] + dy[z]
            if 0 <= di < N and 0 <= dj < M:
                if lst2[di][dj] == 0:
                    virus_lst.append((di, dj))
                    lst2[di][dj] = 2

    count = 0

    for a in range(N):
        for b in range(M):
            if lst2[a][b] == 0:
                count += 1
    result.append(count)

print(max(result))