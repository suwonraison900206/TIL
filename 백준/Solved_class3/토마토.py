M, N, H = map(int,input().split())
lst2 = []
for i in range(H):
    lst = [list(map(int,input().split())) for _ in range(N)]
    lst2.append(lst)

stack = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dz = [1, -1, 0]


for i in range(H):
    for j in range(N):
        for k in range(M):

            if lst2[i][j][k] == 1:
                stack.append([j,k,i])

stack2 = []
cnt = 0
while stack:
    x, y, z = stack.pop()
    for j in range(4):
        di = x + dx[j]
        dj = y + dy[j]
        dw = z

        if -1 < di < N and -1 < dj < M and lst2[dw][di][dj] == 0:
            lst2[dw][di][dj] = 1
            stack2.append([di, dj, dw])
    for w in range(2):
        di = x
        dj = y
        dw = z + dz[w]

        if -1 < dw < H and lst2[dw][di][dj] == 0:
            lst2[dw][di][dj] = 1
            stack2.append([di, dj, dw])

    if not stack and stack2:
        stack = stack2[:]
        stack2 = []
        cnt += 1
flag = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if lst2[i][j][k] == 0:
                flag = 1

if flag ==1 :
    print(-1)
else:
    print(cnt)









