N = int(input())

result = []
cnt = 0
while True:
    if N <3:
        break

    if N % 5 == 0:
        cnt += N // 5
        N = 0
        break

    else:
        N -= 3
        cnt +=1

if N != 0:
    print(-1)
else:
    print(cnt)