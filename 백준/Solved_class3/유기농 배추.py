T = int(input())

for t in range(T):

    M, N, K = map(int, input().split())
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    targets = [list(map(int,input().split())) for __ in range(K)]
    lst = [[0] * M for __ in range(N)]
    visit_lst = [[0] * M for __ in range(N)]
    stack = []
    flag = 1
    for x, y in targets:

        lst[y][x] = 1

    for i, cnt in enumerate(lst):

        for j, cnt2 in enumerate(lst[i]):

            if lst[i][j] == 1 and visit_lst[i][j] == 0:
                stack.append((i, j))
                visit_lst[i][j] = flag

                while stack:

                    q, w = stack.pop()
                    for dir in range(4):
                        di = q + dx[dir]
                        dj = w + dy[dir]

                        if -1 < di < N and -1 < dj < M and lst[di][dj] == 1 and visit_lst[di][dj] == 0:

                            visit_lst[di][dj] = 1
                            stack.append((di, dj))

                flag += 1
    print(flag-1)
