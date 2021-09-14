import copy
import sys
sys.stdin = open('빙산.txt')

N, M = list(map(int, input().split()))
data = []
for n in range(N):
    data.append(list(map(int, input().split())))

flag = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
year = 0

while (flag == 0):
    year += 1
    print(year)
    data0 = copy.deepcopy(data)
    zerocnt = 0
    for n in range(N):
        for m in range(M):
            if data0[n][m] != 0:
                cnt = 0
                for i in range(4):
                    A = n + dx[i]
                    B = m + dy[i]
                    if 0 <= A <= N - 1 and 0 <= B <= M - 1 and data0[A][B] == 0:
                        cnt += 1
                data[n][m] -= cnt
                if data[n][m] < 0:
                    data[n][m] = 0
            else:
                zerocnt += 1

    if zerocnt == (N ) * (M ):
        print(0)
        break
    print(zerocnt)
    visited = [[0] * M for _ in range(N)]
    c = 0
    for n in range(N):
        for m in range(M):
            if visited[n][m] == 0 and data[n][m] != 0:
                c += 1
                if c >= 2:
                    break
                stack = [[n, m]]
                while (stack):
                    a, b = stack.pop()
                    visited[a][b] = 1
                    for i in range(4):
                        A = a + dx[i]
                        B = b + dy[i]
                        if 0 <= A <= N - 1 and 0 <= B <= M - 1 and data[A][B] != 0 and visited[A][B] == 0:
                            stack.append([A, B])
        if c >= 2:
            break

    if c >= 2:
        print(year)
        break

    # 돌아보기
