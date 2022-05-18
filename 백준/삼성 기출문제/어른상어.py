import sys
sys.stdin = open("어른상어.txt", 'r', encoding='UTF8')

N, M, K = map(int,input().split())
shark_map = [list(map(int, input().split())) for __ in range(N)]
each_shark_dir = list(map(int, input().split()))
each_shark_dir_pr = [list(map(int, input().split())) for __ in range(M * M)]
each_shark_dir_pr2 = []
dir = [(0), (-1,0),(1,0),(0,-1),(0,1)]
shark = M
count = 1
for i in range(N):
    for j in range(N):
        if shark_map[i][j] == 0:
            shark_map[i][j] = [shark_map[i][j], 0, 0, 0]
        else:
            for q in range(1, 5):
                if shark_map[i][j] == q:
                    shark_map[i][j] = [shark_map[i][j], each_shark_dir[q-1], K, shark_map[i][j]]
for i in range(4):
    each_shark_dir_pr2.append(each_shark_dir_pr[4*i:(4*i)+4])

while shark != 1 or count < 1001 :
    number = 1
    while number < M+1:
        for i in range(N):
            for j in range(N):
                if shark_map[i][j][0] == number:
                    # check = shark_map[i][j][1]
                    check = 0
                    for q in range(4):
                        di = i + dir[q]
                        dj = j + dir[q]
                        if 0 <= di < N and 0 <= dj < N and shark_map[di][dj][0] == 0:
                            count += 1
                    if check == 0:

                    elif check == 1:

                    else:




                    # shark_map[di][dj][0] = number
                    # shark_map[di][dj][1] = shark_map[i][j][1]
                    # shark_map[di][dj][2] = K
                    # shark_map[i][j][0] = 0








