import sys
sys.stdin = open("4875.txt")
t = int(input())
for test_case in range(t):
    a = int(input())

    list_j = [[1] * (a + 2) for _ in range(a+2)]
    list_k = [list(map(int, input())) for _ in range(a)]
    for i in range(len(list_k)):
        for j in range(len(list_k)):
            list_j[i+1][j+1] = list_k[i][j]



    visit = [[0] * (a + 2) for _ in range(a + 2)]
    stack = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    entry_x, entry_y = 0, 0
    for i in range(len(list_j)):
        for j in range(len(list_j)):
            if list_j[i][j] == 2:
                entry_x = i
                entry_y = j
                break
    stack.append((entry_x, entry_y))
    while stack:
        v = stack.pop()
        if list_j[v[0]][v[1]] == 3:
            cnt = cnt +1
            break
        elif list_j[v[0]][v[1]] != 1:
            for d in range(4):
                di = v[0] + dx[d]
                dj = v[1] + dy[d]

                if list_j[di][dj] != 1 and visit[di][dj] == 0:
                    visit[di][dj] = 1
                    stack.append((di, dj))

    print('#{} {}'.format(test_case+1,cnt))
