import sys
sys.stdin = open("vacumn.txt")

N, M = map(int,input().split())
r, c, d = map(int,input().split())
map_lst = [list(map(int,input().split())) for __ in range(N)]
visit_lst = [[0] * M for __ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
stack = []
stack.append((r,c))
sum = 0

while stack:
    count = 0
    k = stack.pop()
    if visit_lst[k[0]][k[1]] == 0:
        visit_lst[k[0]][k[1]] = 1
        sum = sum + 1

    for i in range(4):
        d = d - 1

        if d == -1:
            d = 3
        di = k[0] + dx[d]
        dj = k[1] + dy[d]

        if map_lst[di][dj] == 0 and visit_lst[di][dj] == 0:
            stack.append((di,dj))
            count = 1
            break

    if count == 0:
        di = k[0] - dx[d]
        dj = k[1] - dy[d]

        if map_lst[di][dj] != 1:
            stack.append((di,dj))

        else:
            break

print(sum)







