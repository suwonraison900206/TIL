import sys
sys.stdin = open("dragon.txt", 'r')
N = int(input())
dx =[1, 0, -1, 0]
dy =[0, -1, 0, 1]
arr =[[0] * 101 for _ in range(101)]
for i in range(N):
    x, y, d, g = list(map(int,input().split()))
    stack = []
    arr[x][y] = 1
    list_d = [d]
    for i in range(g):
        rev_k = list_d[::-1]
        for j in range(len(rev_k)):
            if rev_k[j] +1 == 4:
                rev_k[j] = -1
            list_d = list_d + [rev_k[j] +1]
    for codeness in range(len(list_d)):
        if list_d[codeness] == 0:
            di = x + dx[0]
            dj = y + dy[0]
            arr[di][dj] += 1
            x = di
            y = dj
        elif list_d[codeness] == 1:
            di = x + dx[1]
            dj = y + dy[1]
            arr[di][dj] += 1
            x = di
            y = dj
        elif list_d[codeness] == 2:
            di = x + dx[2]
            dj = y + dy[2]
            arr[di][dj] += 1
            x = di
            y = dj
        elif list_d[codeness] == 3:
            di = x + dx[3]
            dj = y + dy[3]
            arr[di][dj] += 1
            x = di
            y = dj

result = 0
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[i][j] != 0 and arr[i+1][j] != 0 and arr[i][j+1] != 0 and arr[i+1][j+1] != 0:
            result = result + 1

print(result)
















