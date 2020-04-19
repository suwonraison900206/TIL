import sys
sys.stdin = open("pipe.txt")
def h(x, y): # 가로 함수
    global cnt
    if (x, y) == (N-1, N-1):
        cnt = cnt + 1
    else:
        # 가로랑 대각선 가능
        # 첫번째 가로
        if y + 1 <= N-1 and list_k[x][y+1] == 0:
            h(x, y+1)
            if x + 1 <= N-1 and list_k[x+1][y] == 0 and list_k[x+1][y+1] == 0:
                dia(x+1, y+1)
def v(x, y): # 세로 함수
    global cnt
    if (x, y) == (N-1, N-1):
        cnt = cnt +1
    else:
        if x + 1 <= N - 1 and list_k[x+1][y] == 0:
            v(x+1, y)
            if y + 1 <= N-1 and list_k[x][y+1] == 0 and list_k[x+1][y+1] == 0:
                dia(x+1, y+1)
def dia(x, y): # 대각선 함수
    global cnt
    if (x, y) == (N-1, N-1):
        cnt = cnt + 1
    if y + 1 <= N-1 and list_k[x][y+1] == 0:
        h(x, y+1)
    if x + 1 <= N - 1 and list_k[x+1][y] == 0:
        v(x+1, y)
    if y + 1 <= N-1 and list_k[x][y+1] == 0 and x + 1 <= N - 1 and list_k[x+1][y] == 0 and list_k[x+1][y+1] == 0:
        dia(x+1, y+1)

N = int(input())
list_k = []
cnt = 0
for i in range(N):
    temp = list(map(int,input().split()))
    list_k.append(temp)
if list_k[0][2] == 0:
    h(0, 2)
    if list_k[1][1] == 0 and list_k[1][2] == 0:
        dia(1, 2)
print(cnt)









