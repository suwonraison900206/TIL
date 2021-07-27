import sys
sys.stdin = open('행성 터널.txt')

N = int(input())
print(N)
codes = [list(map(int,input().split())) for __ in range(N)]
x = []
y = []
z = []
cnt = 1
for a,b,c, in codes:

    x.append([a,cnt])
    y.append([b,cnt])
    z.append([c,cnt])
    cnt +=1
print(x)
x.sort(key=lambda x: x[0])
print(x)
print(y)
y.sort(key=lambda x: x[0])
print(y)
print(z)
z.sort(key=lambda x: x[0])
print(z)