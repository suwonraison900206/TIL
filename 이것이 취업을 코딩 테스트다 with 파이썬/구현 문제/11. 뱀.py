import sys
sys.stdin = open("11. 뱀.txt")

N = int(input())
K = int(input())
apple_lst = [list(map(int,input().split())) for __ in range(K)]
L = int(input())
dir_lst = [list(input().split()) for __ in range(L)]
wall = [[2] * (N+2)]
board = wall + [([2] + ([0] * N) + [2]) for __ in range(N)] + wall
for i in range(len(apple_lst)):
    board[apple_lst[i][0] ][apple_lst[i][1] ] = 1
time = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_num = 0
snake = [[1,1]]

while True:
    k = snake[-1]
    tail = snake.pop(0)

    if len(dir_lst) != 0 and time == int(dir_lst[0][0]):
        if dir_lst[0][1] == 'D':
            if dir_num != 3:
                dir_num = dir_num + 1
            elif dir_num == 3:
                dir_num = 0
            dir_lst.pop(0)
        elif dir_lst[0][1] == 'L':
            if dir_num != 0:
                dir_num = dir_num - 1
            elif dir_num == 0:
                dir_num = 3
            dir_lst.pop(0)

    di = k[0] + dx[dir_num]
    dj = k[1] + dy[dir_num]

    if [di, dj] in snake or [di,dj] == tail:
        break
    elif board[di][dj] == 0:
        snake.append([di, dj])
    elif board[di][dj] == 1:
        snake.insert(0, tail)
        snake.append([di, dj])
        board[di][dj] = 0
    elif board[di][dj] == 2:
        break

    time = time + 1


print(time + 1)