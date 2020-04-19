import sys
sys.stdin = open("research.txt")

K, N, M = list(map(int, input().split()))
result = []
sample_list =[]
for i in range(K):
    result.append(list(map(int, input().split())))
    for j in range(len(result)):
        sample_list.append(result[j])
    result = []

k = []
final = []

for i in range(K):
    for j in range(N):
        k.append([sample_list[i][j]] + [0]) # 삼중배열 모든 값에 [0] 붙여주기
    final.append(k)
    k = []


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

air_con = []
for i in range(K):
    for j in range(N):
        if final[i][j][0] == -1:
            air_con.append(i)
            air_con.append(j)

for q in range(M):
    for i in range(K):
        for j in range(N):
            if final[i][j][0] != 0 and final[i][j][0] != -1:
                div = (final[i][j][0] // 5)
                for d in range(4):
                    di = i + dx[d]
                    dj = j + dy[d]
                    h = 0

                    while 0 <= di <= K-1 and 0 <= dj <= N-1 and final[di][dj][0] != -1 and h < 1:
                        final[di][dj][1] = final[di][dj][1] + div
                        final[i][j][0] = final[i][j][0] - div
                        h = h + 1


    # 나눠져 있는 값 합쳐줌
    for i in range(K):
        for j in range(N):
            final[i][j][0] = final[i][j][0] + final[i][j][1]
            final[i][j][1] = 0






    for i in range(air_con[0]-1,-1,-1):
        if final[i+1][0][0] == -1:
            final[i][0][0] = 0
        else:
            final[i+1][0][0] = final[i][0][0]
            final[i][0][0] = 0

    for i in range(1,N):
        final[0][i-1][0] = final[0][i][0]
        final[0][i][0] = 0

    for i in range(1, air_con[0]+1):
        final[i-1][N-1][0] = final[i][N-1][0]
        final[i][N-1][0] = 0

    for i in range(N-2,0,-1):
        final[air_con[0]][i+1][0] = final[air_con[0]][i][0]
        final[air_con[0]][i][0] = 0

    for i in range(air_con[2]+1, K):
        if final[i-1][0][0] == -1:
            final[i][0][0] = 0
        else:
            final[i-1][0][0] = final[i][0][0]
            final[i][0][0] = 0

    for i in range(1, N):
        final[K-1][i-1][0] = final[K-1][i][0]
        final[K-1][i][0] = 0

    for i in range(K-2, air_con[2]-1, -1):
        final[i+1][N-1][0] = final[i][N-1][0]
        final[i][N-1][0] = 0

    for i in range(N-2, 0, -1):
        final[air_con[2]][i+1][0] = final[air_con[2]][i][0]
        final[air_con[2]][i][0] = 0

cnt = 0
for i in range(K):
    for j in range(N):
        if final[i][j][0] != -1:
            cnt = cnt + final[i][j][0]

print(cnt)
#
