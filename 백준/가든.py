import sys
sys.stdin = open("garden.txt")

N, M, G, R = map(int,input().split())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))

cnt = []

for i in range(N):
    for j in range(M):
        if lst[i][j] == 2:
            cnt.append([i,j])
print(cnt)
