N, M = map(int,input().split())
lst = [list(map(int,input().split())) for __ in range(N)]
map_lst = [[0] * (M+6) for __ in  range(N+6)]

for i in range(3,3+N):
    for j in range(3, 3+M):

        map_lst[i][j] = lst[i-3][j-3]

a = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
b = [[1, 1], [1, 1]]
c = [[1, 0, 0], [1, 0, 0], [1, 1, 0]]
d = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]
u = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
result = 0
for i in range(4): # 90 도 회전 시키면서 전부 탐색
    a = [list(reversed(i)) for i in zip(*a)]
    b = [list(reversed(i)) for i in zip(*b)]
    c = [list(reversed(i)) for i in zip(*c)]
    c_reversed = [list(reversed(i)) for i in zip(*c)][::-1]
    d = [list(reversed(i)) for i in zip(*d)]
    d_reversed = [list(reversed(i)) for i in zip(*d)][::-1]
    u = [list(reversed(i)) for i in zip(*u)]

    for q in range(len(map_lst)-4):
        for w in range(len(map_lst[q]) -4):
            cnt = 0
            for e in range(q, q + len(a)):
                for r in range(w, w+ len(a)):

                    if map_lst[e][r] != 0 and a[e-q][r-w] == 1:
                        cnt = cnt + map_lst[e][r]

            if cnt > result:
                result = cnt

    for q in range(2, len(map_lst)-2):
        for w in range(2, len(map_lst[q]) -2):
            cnt = 0
            for e in range(q, q + len(b)):
                for r in range(w, w+ len(b)):
                    if map_lst[e][r] != 0:
                        cnt = cnt + map_lst[e][r]

            if cnt > result:
                result = cnt

    for q in range(len(map_lst) - 3):
        for w in range(len(map_lst[q]) - 3):
            cnt = 0
            for e in range(q, q + len(c)):
                for r in range(w, w + len(c)):

                    if c[e - q][r - w] == 1:
                        cnt = cnt + map_lst[e][r]

            if cnt > result:
                result = cnt

    for q in range(len(map_lst) - 3):
        for w in range(len(map_lst[q]) - 3):
            cnt = 0
            for e in range(q, q + len(c)):
                for r in range(w, w + len(c)):

                    if c_reversed[e - q][r - w] == 1:
                        cnt = cnt + map_lst[e][r]

            if cnt > result:
                result = cnt

    for q in range(len(map_lst) - 3):
        for w in range(len(map_lst[q]) - 3):
            cnt = 0
            for e in range(q, q + len(d)):
                for r in range(w, w + len(d)):
                    if d[e - q][r - w] == 1:
                        cnt = cnt + map_lst[e][r]

            if cnt > result:
                result = cnt

    for q in range(len(map_lst) - 3):
        for w in range(len(map_lst[q]) - 3):
            cnt = 0
            for e in range(q, q + len(c)):
                for r in range(w, w + len(c)):

                    if d_reversed[e - q][r - w] == 1:
                        cnt = cnt + map_lst[e][r]

            if cnt > result:
                result = cnt

    for q in range(len(map_lst) - 3):
        for w in range(len(map_lst[q]) - 3):
            cnt = 0
            for e in range(q, q + len(u)):
                for r in range(w, w + len(u)):
                    if u[e - q][r - w] == 1:
                        cnt = cnt + map_lst[e][r]

            if cnt > result:
                result = cnt

print(result)