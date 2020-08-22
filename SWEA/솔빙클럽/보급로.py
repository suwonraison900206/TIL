import sys
from _collections import deque
sys.stdin = open("보급로.txt")

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    map_lst = [list(map(int,input())) for __ in range(N)]
    map_lst2 =[[99999] * N for __ in range(N)]
    map_lst2[0][0] = 0

    stack = deque()
    stack.append([0,0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while stack:
        x, y = stack.popleft()
        for i in range(4):
            x_codeness = x + dx[i]
            y_codeness = y + dy[i]
            if 0 <= x_codeness <= N-1 and 0 <= y_codeness <= N-1:
                if map_lst2[x_codeness][y_codeness] > map_lst[x_codeness][y_codeness] + map_lst2[x][y]: # 기존값이 새로운 거보다 크면 갈아 끼움
                    map_lst2[x_codeness][y_codeness] = map_lst[x_codeness][y_codeness] + map_lst2[x][y]
                    stack.append([x_codeness, y_codeness])


    print('#{} {}'.format(test_case, map_lst2[N-1][N-1]))








