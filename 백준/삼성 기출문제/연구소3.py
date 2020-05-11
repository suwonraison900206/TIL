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
final_result = []

for i in range(len(k)):
    lst2 = copy.deepcopy(lst)
    stack = []
    stack2 = []
    stack3 = []
    count = 0
    count2 =0
    for j in range(M):
        lst2[k[i][j][0]][k[i][j][1]] = 3
        stack.append((k[i][j][0], k[i][j][1]))
    while stack:
        q = stack.pop()
        for i in range(4):
            di = q[0] + dx[i]
            dj = q[1] + dy[i]
            if 0 <= di < N and 0 <= dj < N:
                if lst2[di][dj] == 0:
                    lst2[di][dj] = 3
                    stack2.append((di,dj))
                elif lst2[di][dj] == 2:
                    lst2[di][dj] = 3
                    stack3.append((di,dj))

        if len(stack) == 0:
            if len(stack2) != 0:
                stack = stack2[:]
                stack2 = []
                stack.extend(stack3[:])
                stack3 = []
                count = count + 1
            elif len(stack2) == 0 and len(stack3) != 0:
                for v in range(N):
                    for w in range(N):
                        if lst2[v][w] == 0:
                            count2 = count2 + 1
                if count2 != 0:
                    stack = stack3[:]
                    stack3 = []
                    count = count + 1
                else:
                    stack = stack3[:]
                    stack3 = []

    for i in range(N):
        for j in range(N):
            if lst2[i][j] == 0:
                count = 10000

    final_result.append(count)

if min(final_result) == 10000:
    print(-1)
else:
    print(min(final_result))






