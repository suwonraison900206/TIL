import sys
sys.stdin = open('미로탐색.txt')

N, M = map(int,input().split())

arr = [list(map(int, input())) for __ in range(N)]
visit_arr = [[0] * M for __ in range(N)]
print(visit_arr)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
stack = [[0,0]]
stack2 = []
visit_arr[0][0] = 1
cnt = 0
while stack:
    x, y = stack.pop()
    if [x,y] == [N-1, M-1]:
        break

    for i in range(4):
        di = x + dx[i]
        dj = y + dy[i]


        if -1 < di < N and -1 < dj < M and arr[di][dj] == 1 and visit_arr[di][dj] == 0:

            visit_arr[di][dj] = 1
            stack2.append([di,dj])

    if not stack and stack2:
  
        stack = stack2[:]
        stack2 = []
        cnt +=1
print(cnt+1)