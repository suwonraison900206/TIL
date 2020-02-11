#사방을 탐색하기 위한 델타
#위, 오른,아래, 왼
di = [-1, 0, 1, 0]
dj =[0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0    #최대값 구하기 위한 변수
    for i in range(N):
        for j in range(M):
            k = arr[i][j]   # 현재위치의 꽃가루 수
            sum = k         # 꽃가루 누적합 할 변수 : sum
                            # 현위치 꽃가루 더함
            for d in range(4):
                ni,nj = i+di[d],j+dj[d] #새로운 탐색구역 계산
                h = 1       #탐색 깊이
                while 0 <= ni < N and 0 <= nj < M and h <= k:  #배열 내부인지
                    sum = sum + arr[ni][nj]
                    ni += di[d] #이미 정해진 방향으로 더 탐색
                    nj += dj[d]
                    h += 1
            #여기 -> 하나의 좌표에 대해서 누적합 완료
            if maxV < sum:
                maxV = sum
    print('#{} {}'.format(tc, maxV))
                    
                












