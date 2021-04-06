import sys
from itertools import permutations
import copy
sys.stdin = open('사다리 조작.txt')

N, M, H = map(int,input().split())
nodes = [list(map(int,input().split())) for __ in range(M)]
for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        nodes[i][j] = nodes[i][j] -1

ladders = [[0] * N for __ in range(M)]

for node in nodes:
    ladders[node[0]][node[1]] = 1
    ladders[node[0]][node[1]+1] = 1

for i in range(len(nodes)):
    x,y = nodes[i]
    nodes.append([x, y+1])
nodes.sort()
possible_lst = []
for i in range(len(ladders)):
    for j in range(0,len(ladders[i])-1):

        if [i,j] not in nodes and [i, j+1] not in nodes:
            possible_lst.append([i,j])

print(possible_lst, 'possible')
# print(nodes, 'nodes')
# print(ladders, 'ladders')
for q in range(0,4):
    for w in permutations(possible_lst,q):
        ladder = copy.deepcopy(ladders)
        for r in range(len(w)):
            ladder[w[r][0]][w[r][1]] = 1
            ladder[w[r][0]][w[r][1]+1] = 1
        flag = 0

        for i in range(N):

            start = [[0, i]]
            x, y = start.pop()
            while True:
                if [x,y] in nodes:
                    if y+1 < N and ladder[x][y+1] == 1:
                        y = y+1
                    elif y -1 >= 0 and ladder[x][y-1] == 1:
                        y = y - 1

                    if x < M -1:
                        x = x + 1
                    else:
                        print(i, y)
                        if y != i:
                            flag = 1
                            break
                        else:
                            break
                else:
                    if x < M-1:
                        x = x+1
                    else:
                        print(i, y)
                        if y != i:
                            flag = 1
                            break
                        else:
                            break
        if flag == 0:
            print(123)