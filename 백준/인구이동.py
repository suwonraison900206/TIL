import sys
sys.stdin = open('인구이동.txt')

N, L, R = map(int,input().split())
C_map = [list(map(int,input().split())) for __ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
final = 0

while True:
    visit_map = [[0] * N for _ in range(N)]
    stack = []
    cnt = 1
    count_lst = []
    for i in range(N):
        for j in range(N):
            if visit_map[i][j] == 0:
                visit_map[i][j] = cnt
                stack.append((i,j))
                count = C_map[i][j]
                number = 1
                while stack:
                    x, y = stack.pop()
                    for q in range(4):
                        di = x + dx[q]
                        dj = y + dy[q]

                        if 0 <= di < N and 0 <= dj < N and visit_map[di][dj] == 0:
                            if L <= abs(C_map[x][y] - C_map[di][dj]) <= R:
                                visit_map[di][dj] = cnt
                                stack.append((di,dj))
                                number += 1
                                count = count + C_map[di][dj]

                if number != 1:
                    count_lst.append([cnt,count, number])
                    cnt += 1
                else:
                    cnt += 1

    if not count_lst:
        print(final)
        break


    for w in range(len(count_lst)):
        for i in range(N):
            for j in range(N):
                if visit_map[i][j] == count_lst[w][0]:
                    C_map[i][j] = count_lst[w][1] // count_lst[w][2]

    final +=1









