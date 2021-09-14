import copy
import sys
sys.stdin = open('빙산.txt')

N, M = map(int,input().split())
lst = [list(map(int,input().split())) for __ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
flag = 0
while True:
    visit_lst = [[0] * M for __ in range(N)]
    lst2 = copy.deepcopy(lst)
    print(lst2)
    check = 0

    for i in range(N):
        for j in range(M):

            if lst2[i][j] != 0:
                flag = 0

                for q in range(4):
                    di = i + dx[q]
                    dj = j + dy[q]

                    if -1 < di < N and -1 < dj < M and lst2[di][dj] == 0:
                        flag +=1

                lst[i][j] -= flag
                if lst[i][j] < 0:
                    lst[i][j] = 0

    for i in range(N):
        for j in range(M):
            if lst[i][j] != 0:
                if visit_lst[i][j] == 0:
                    check +=1
                    visit_lst[i][j] = check
                    stack = [[i,j]]
                    while stack:

                        x, y = stack.pop()
                        for q in range(4):
                            di = x + dx[q]
                            dj = y + dy[q]

                            if -1 < di < N and -1 < dj < M and lst[di][dj] != 0 and visit_lst[di][dj] == 0:

                                visit_lst[di][dj] = check
                                stack.append([di, dj])


    cnt +=1

    if check > 1:

        break
    elif check == 0:
        flag = 1
        break

if flag == 1:
    print(0)
else:
    print(cnt)