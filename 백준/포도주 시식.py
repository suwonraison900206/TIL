import sys
sys.stdin = open("포도주 시식.txt")

n = int(input())

wine = []

for i in range(n):
    wine.append(int(input()))

d = [0] * (n +1)

try:
    d[1] = wine[0]
    d[2] = wine[0] + wine[1]
    d[3] = max(wine[0] + wine[2], wine[1]+wine[2])
    d[4] = max(wine[0] + wine[1] + wine[3], wine[0]+wine[2]+wine[3])
except:
    pass
for i in range(5, n+1):
    try:
        print(d)
        print(wine)
        d[i] = max(d[i-4] + wine[i-2] +wine[i-1], d[i-3]+wine[i-1],)
    except:
        d[i] = 0
print(d)