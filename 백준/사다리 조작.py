import sys
from itertools import permutations
import copy
sys.stdin = open('사다리 조작.txt')


nodes = [list(map(int,input().split())) for __ in range(M)]
for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        nodes[i][j] = nodes[i][j] -1

ladders = [[0] * N for __ in range(M)]

for node in nodes:
    ladders[node[0]][node[1]] = 1
    ladders[node[0]][node[1]+1] = 2

print(nodes)
possible_lst = []

for i in range(0, H):
    for j in range(0, M):
        if j == 0:
            if [i,j] not in nodes and [i,j+1] not in nodes:
                possible_lst.append([i,j])
        else:
            if [i,j] not in nodes and [i,j-1] not in nodes and [i,j+1] not in nodes:
                possible_lst.append([i,j])

print(possible_lst, '123123')

for w in range(4):
    for r in permutations(possible_lst,w):
        ladder = copy.deepcopy(ladders)
        copy_nodes = copy.deepcopy(nodes)
        qq = 0

        print(r)
        if len(r) !=0:
            for t in r:
                if [t[0], t[1]] not in copy_nodes and [t[0], t[1] -1] not in copy_nodes and [t[0], t[1] +1] not in copy_nodes:
                    copy_nodes.append([t[0], t[1]])
                    ladder[t[0]][t[1]] = 1
                    ladder[t[0]][t[1]+1] = 2
                else:
                    qq = 1
        if qq == 1:
            continue

        flag = 0
        print(r)
        for i in range(N):
            x = 0
            y = i
            while True:

                if ladder[x][y] == 0:
                    x += 1
                elif ladder[x][y] == 1:
                    x += 1
                    y += 1
                elif ladder[x][y] == 2:
                    x += 1
                    y -= 1

                if x == N-1:
                    if ladder[x][y] == 0:
                        if y == i:
                            print('True', y,i)
                        else:
                            flag = 1
                        break
                    elif ladder[x][y] == 1:
                        y += 1
                        if y == i:
                            print('True', y, i)
                            pass
                        else:
                            flag = 1
                        break

                    elif ladder[x][y] == 2:
                        y -=1
                        if y == i:
                            print('True', y, i)
                            pass
                        else:
                            flag = 1
                        break



        if flag == 0:
            print(w)