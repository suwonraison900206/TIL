N = int(input())

q = str(N).split()


minimun = N - (len(q[0]) * 9)


b = 12

c = list(str(b))

if minimun < 0:
    cnt = 0
    for i in range(1 , N):
        cnt = i
        c = list(str(i))

        for q in c:
            cnt = cnt + int(q)

        if cnt == N:
            print(i)
            break
    else:
        print(0)
else:
    cnt = 0
    for i in range(minimun , N):
        cnt = i
        c = list(str(i))

        for q in c:
            cnt = cnt + int(q)

        if cnt == N:
            print(i)
            break
    else:
        print(0)


