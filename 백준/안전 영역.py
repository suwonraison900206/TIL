import copy
import sys
sys.stdin = open("안전영역.txt")

N = int(input())
map = [list(map(int,input().split())) for __ in range(N)]
lst_map = [[0] * N for __ in range(N)]
map_max = 0
map_min = float('inf')
dx = [-1,0,1,0]
dy = [0,1,0,-1]
count = 0
for i in map:
    if max(i) > map_max:
        map_max = max(i)
    if min(i) < map_min:
        map_min = min(i)

for i in range(map_min, map_max +1):
    map2 = copy.deepcopy(map)
    lst_map2 = copy.deepcopy(lst_map)
    cnt = 10
    flag = 0
    stack = []
    for j in range(len(map2)):
        for k in range(len(map2)):

            if map2[j][k] <= i:
                map2[j][k] = 0

    for j in range(len(map2)):
        for k in range(len(map2)):

            if map2[j][k] != 0 and lst_map2[j][k] == 0:
                lst_map2[j][k] = cnt
                stack.append([j,k])

                while stack:
                    x, y = stack.pop()
                    for q in range(4):
                        di = x + dx[q]
                        dj = y + dy[q]

                        if -1 < di < N and -1 < dj < N and map2[di][dj] != 0 and lst_map2[di][dj] == 0:

                            lst_map2[di][dj] = cnt
                            stack.append([di, dj])

                cnt +=1
                flag +=1

    if count < flag:
        count = flag
if count == 0:
    print(1)
else:
    print(count)


