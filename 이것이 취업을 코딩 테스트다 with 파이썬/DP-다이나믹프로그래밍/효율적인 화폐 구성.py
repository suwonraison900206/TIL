N, M = map(int,input().split())

coin = []

for i in range(N):
    coin.append(int(input()))

d = [0] * 10001

d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2
d[6] = 2
d[7] =