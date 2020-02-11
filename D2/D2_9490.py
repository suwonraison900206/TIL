import sys
sys.stdin = open("누적합.txt")

# # 사방을 탐색하기 위한 델타
# # 위, 오른,아래, 왼
# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     maxV = 0  # 최대값 구하기 위한 변수
#     for i in range(N):
#         for j in range(M):
#             k = arr[i][j]  # 현재위치의 꽃가루 수
#             sum = k  # 꽃가루 누적합 할 변수 : sum
#             # 현위치 꽃가루 더함
#             for d in range(4):
#                 ni, nj = i + di[d], j + dj[d]  # 새로운 탐색구역 계산
#                 h = 1  # 탐색 깊이
#                 while 0 <= ni < N and 0 <= nj < M and h <= k:  # 배열 내부인지
#                     sum = sum + arr[ni][nj]
#                     ni += di[d]  # 이미 정해진 방향으로 더 탐색
#                     nj += dj[d]
#                     h += 1
#             # 여기 -> 하나의 좌표에 대해서 누적합 완료
#             if maxV < sum:
#                 maxV = sum
#     print('#{} {}'.format(tc, maxV))
#
#
#
#
#
#

t = int(input())

for test_case in range(t):
    N, M = map(int, input().split())
    sample_list = [list(map(int,input().split())) for _ in range(N)]


    dx =[-1, 1, 0, 0]   #상 하 좌 우
    dy =[0, 0, -1, 1]


    sum = 0
    maxv = 0
    for i in range(N):
        for j in range(M):
            sum = sample_list[i][j]
            k = sum
            for d in range(4):
                di = i + dx[d]
                dj = j + dy[d]
                h = 1

                while 0 <= di < N and 0 <= dj < M and h <= k:
                    sum = sum + sample_list[di][dj]
                    di = di + dx[d]
                    dj = dj + dy[d]
                    h = h +1
                if maxv < sum:
                    maxv = sum

    print('#{} {}'.format(test_case+1, maxv))















































    # dx = [-1, 1, 0, 0]
    # dy = [0, 0, -1, 1]
    # maxv = 0
    # for i in range(N):
    #     for j in range(M):
    #         k = sample_list[i][j]
    #         sum = k
    #
    #         for d in range(4):
    #             di = i + dx[d]
    #             dj = j + dy[d]
    #
    #             h = 1
    #             while 0 <= di < N and 0 <= dj < M and h <= k:
    #                 sum = sum + sample_list[di][dj]
    #                 di = di + dx[d]
    #                 dj = dj + dy[d]
    #                 h = h + 1
    #         if maxv < sum:
    #             maxv = sum
    #
    print('#{} {}'.format(test_case+1, maxv))
    #
    #
    #
    #













