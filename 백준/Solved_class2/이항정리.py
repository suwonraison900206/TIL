N, K = map(int,input().split())
a = abs(N-K)
b = 1
c = 1

for i in range(1,N+1):

    b *= i

for i in range(1, K+1):

    c *= i
d = 1
for i in range(1, a+1):
    d *= i

d = b / (c * d)
print(int(d))