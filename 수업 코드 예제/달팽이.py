
N = int(input())
lst = [[0] * N for __ in range(N)]
cnt = 1
lst[0][0] = cnt # 1부터 시작
dx = [0, 1, 0, -1] # [→ , ↓ , ← , ↑]
dy = [1, 0, -1, 0] # [→ , ↓ , ← , ↑]
dir = 0 # 방향 바꿔줄 변수

stack = [[0,0]] # (0,0) 부터 시작

while stack:
    if cnt == N * N: # 정사각형 배열이니까 N * N 이 최고값, 즉 모든 곳에 방문 함
        break
    x, y = stack.pop()
    di = x + dx[dir]
    dj = y + dy[dir]

    if 0 <= di < N and 0 <= dj < N and lst[di][dj] == 0: # 리스트 범위를 벗어나지 않고 , lst 값이 0인 곳 즉 한번도 탐색 안된 곳일 때만 들어가짐
        cnt +=1
        lst[di][dj] = cnt
        stack.append([di,dj])
    else: # 리스트 범위를 벗어났거나 , 이미 탐색된 곳을 갔으므로 방향 바꿔줌
        dir +=1
        if dir == 4:
            dir = 0
        stack.append([x,y])

print(lst)

