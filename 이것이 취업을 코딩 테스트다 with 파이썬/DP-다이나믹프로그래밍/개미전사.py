N = int(input())
K = list(map(int,input().split()))

d = [0] * 101

d[0] = K[0]
d[1] = K[1]

for i in range(2, N):
    d[i] = max(d[i-1] , d[i-2] + K[i])

print(d[N-1])