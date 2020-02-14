

N = int(input())

for i in range(1, N):
    print('*' * i)

for j in range(1):
    print('*' * N)

for k in range(N-1, 0, -1):
    print('*' * k)
