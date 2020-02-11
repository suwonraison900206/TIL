import sys
sys.stdin = open("풍선팡.txt")


a = int(input())

for test_case in range(a):

    N, M = map(int,input().split())
    temp = [list(map(int,input().split())) for _ in range(N)]
    dx =[-1, 1, 0, 0]
    dy =[0, 0, -1, 1]

    maxv=0
    for i in range(N):
        for j in range(M):
            sum = temp[i][j]
            k = sum

            for d in range(4):
                di = i + dx[d]
                dj = j + dy[d]
                h = 1

                while 0 <= di < N and 0 <= dj < M and h <= k:
                    sum = sum + temp[di][dj]
                    di = di + dx[d]
                    dj = dj + dy[d]
                    h = h + 1

                if maxv < sum:
                    maxv = sum

    print('#{} {}'.format(test_case+1, maxv))







