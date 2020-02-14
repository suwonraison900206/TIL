import sys
sys.stdin = open("1226.txt")
t = 10
for test_case in range(t):
    a = int(input())
    b = [list(map(int, input())) for _ in range(16)]

    stack = []

    visit = [[0] * 16 for _ in range(16)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    for i in range(16):
        for j in range(16):
            if b[i][j] == 2:
                stack.append((i,j))


    while stack:
        v = stack.pop()
        if b[v[0]][v[1]] == 3:
            cnt = cnt + 1
        elif b[v[0]][v[1]] != 1:

            for d in range(4):
                di = v[0] + dx[d]
                dj = v[1] + dy[d]
                if b[di][dj] != 1 and visit[di][dj] == 0:
                    stack.append((di, dj))
                    visit[di][dj] = 1

    print(cnt)







