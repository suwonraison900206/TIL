import sys
sys.stdin = open('구슬탈출.txt')

def push(map_lst, r, b, dir,locate, count):
    global result
    global direction
    global final_lst
    map_lst[r[0]][r[1]] = '.'
    map_lst[b[0]][b[1]] = '.'
    r_count = 0
    b_count = 0
    r_stop = 0
    b_stop = 0

    if count == 11:
        return result

    while b_stop == 0:
        if map_lst[b[0]+dir[0]][b[1]+dir[1]] == '#':
            b_stop = -1
        elif map_lst[b[0]+dir[0]][b[1]+dir[1]] == 'O':
            return result
        elif map_lst[b[0]+dir[0]][b[1]+dir[1]] == '.':
            b = (b[0]+dir[0], b[1]+dir[1])
            b_count += 1

    while r_stop == 0:
        if map_lst[r[0]+dir[0]][r[1]+dir[1]] == '#':
            r_stop = -1
        elif map_lst[r[0]+dir[0]][r[1]+dir[1]] == 'O':
            final_lst.append(count)
            return result
        elif map_lst[r[0]+dir[0]][r[1]+dir[1]] == '.':
            r = (r[0] + dir[0], r[1] + dir[1])
            r_count += 1

    if r == b:
        if r_count > b_count:
            map_lst[b[0]][b[1]] = 'B'
            map_lst[r[0]-dir[0]][r[1]-dir[1]] = 'R'
            r = (r[0]-dir[0], r[1]-dir[1])
        elif r_count < b_count:
            map_lst[r[0]][r[1]] = 'R'
            map_lst[b[0]-dir[0]][b[1]-dir[1]] = 'B'
            b = (b[0]-dir[0], b[1]-dir[1])
    else:
        map_lst[r[0]][r[1]] = 'R'
        map_lst[b[0]][b[1]] = 'B'

    if locate == 0:
        push(map_lst, r, b, direction[1], 1, count + 1)
        push(map_lst, r, b, direction[2], 2, count + 1)
        push(map_lst, r, b, direction[3], 3, count + 1)
    elif locate == 1:
        push(map_lst, r, b, direction[0], 0, count + 1)
        push(map_lst, r, b, direction[2], 2, count + 1)
        push(map_lst, r, b, direction[3], 3, count + 1)
    elif locate == 2:
        push(map_lst, r, b, direction[0], 0, count + 1)
        push(map_lst, r, b, direction[1], 1, count + 1)
        push(map_lst, r, b, direction[3], 3, count + 1)
    elif locate == 3:
        push(map_lst, r, b, direction[0], 0, count + 1)
        push(map_lst, r, b, direction[1], 1, count + 1)
        push(map_lst, r, b, direction[2], 2, count + 1)

N, M = map(int,input().split())
lst = [list(input()) for __ in range(N)]
RED = (0, 0)
BLUE = (0, 0)
exit = (0, 0)
final_lst = []
result = -1
direction = [(-1,0), (1,0), (0,1), (0,-1)]  # 북, 남 , 동, 서

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'B':
            BLUE = (i,j)
        elif lst[i][j] == 'R':
            RED = (i,j)
        elif lst[i][j] == 'O':
            exit = (i,j)

for i in range(4):
    push(lst, RED, BLUE, direction[i],i, 1)

if len(final_lst) == 0:
    print(-1)
else:
    print(min(final_lst))