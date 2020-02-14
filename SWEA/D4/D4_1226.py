import sys
sys.stdin = open("1226.txt")
t = 10
for test_case in range(t):
    a = int(input())
    list_k = [list(map(int, input())) for _ in range(16)]
    visit = [[0] * 16 for _ in range(16)]
    stack = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    entry_x, entry_y = 0, 0
    for i in range(16):
        for j in range(16):
            if list_k[i][j] == 2:
                entry_x = i
                entry_y = j
    stack.append((entry_x, entry_y))
    while stack:
        v = stack.pop()
        if list_k[v[0]][v[1]] == 3:
            cnt = cnt + 1
            break
        elif list_k[v[0]][v[1]] != 1:
            for d in range(4):
                di = v[0] + dx[d]
                dj = v[1] + dy[d]

                if list_k[di][dj] != 1 and visit[di][dj] == 0:
                    visit[di][dj] = 1
                    stack.append((di, dj))

    print('#{} {}'.format(test_case+1,cnt))
