

# 탑 다운 방식으로 피보나치 수열 작성

d = [0] * 1000

def fibo(x):
    if x == 1 or x == 2:
        return 13
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x - 2)
    return d[x]

print(fibo(999))


# 보텀업 방식 으로 피보나치 수열 작성


d = [0] * 1000

d[1] = 1
d[2] = 2

n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])