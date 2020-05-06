import sys
sys.stdin = open("snake.txt")

N = int(input())
K = int(input())
lst = [[0] * N for _ in range(N)]
for i in range(K):
    apple = list(map(int,input().split()))
    lst[apple[0] - 1][apple[1] - 1] = 1

L = int(input())

dir_cnt = []

for i in range(L):
    dir = list(input().split())
    dir[0] = int(dir[0])
    dir_cnt.append(dir)


dx =[0, 1, 0, -1]
dy =[1, 0, -1, 0]
dir = 0
time = 0
snake = []
snake.append([0,0])
while snake:
    di = snake[-1][0] + dx[dir]
    dj = snake[-1][1] + dy[dir]
    time = time + 1
    if di < 0 or di > N-1 or dj < 0 or dj > N-1:
        break
    else:
        if lst[di][dj] == 0:
            if [di, dj] in snake:
                print(time)
                break
            else:
                snake.pop(0)
                snake.append([di,dj])
        elif lst[di][dj] == 1:
            if [di, dj] in snake:
                print(time)
                break
            else:
                snake.append([di,dj])
                lst[di][dj] = 0
    if len(dir_cnt) != 0:
        if dir_cnt[0][0] == time:
            if dir_cnt[0][1] == 'D':
                dir = dir + 1
                if dir == 4:
                    dir = 0
                dir_cnt.pop(0)
            elif dir_cnt[0][1] == 'L':
                dir = dir - 1
                if dir == -1:
                    dir = 3
                dir_cnt.pop(0)







