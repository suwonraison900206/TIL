t = 1

for test_case in range(t):
    k = int(input())
    list_k = [[0] * (k + 2) for _ in range(k + 2)]
    visit = [[0] * (k + 2) for _ in range(k + 2)]
    stack = []
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    entry_x, entry_y = 0, 0
    test_in = []
    result = 0
    final_result = []

    for i in range(k):
        test_in.append(list(map(int, input())))

    for i in range(k):
        for j in range(k):
            list_k[i+1][j+1] = test_in[i][j]

    for i in range(len(list_k)):
        for j in range(len(list_k)):
            if list_k[i][j] == 1 and visit[i][j] == 0:
                final_result.append(result)
                result = 0

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
                                result = result + 1
                                stack.append((di, dj))
    final_result.append(result)

    list.sort(final_result)

    print(cnt)
    for i in range(1, cnt+1):
        print(final_result[i])
