t = int(input())

for test_case in range(t):
    temp = list(map(int, input().split()))
    list_k = [[0] * (temp[0] + 2) for _ in range(temp[1] + 2)]
    visit = [[0] * (temp[0] + 2) for _ in range(temp[1] + 2)]
    stack = []
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    entry_x, entry_y = 0, 0

    for i in range(temp[2]):
        codeness = list(map(int, input().split()))

        list_k[(codeness[1]+1)][(codeness[0] + 1)] = 1



    for i in range(temp[1]+2):
        for j in range(temp[0]+2):
            if list_k[i][j] == 1 and visit[i][j] == 0:
                cnt = cnt + 1
                entry_x = i
                entry_y = j
                stack.append((entry_x, entry_y))
                while stack:
                    v = stack.pop()
                    if list_k[v[0]][v[1]] == 1:
                        for d in range(4):
                            di = v[0] + dx[d]
                            dj = v[1] + dy[d]

                            if list_k[di][dj] == 1 and visit[di][dj] == 0:
                                visit[di][dj] = 1
                                stack.append((di, dj))

    print('{}'.format(cnt))