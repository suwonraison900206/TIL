N = int(input())
if N == 1:
    exit()
while True:

    for i in range(2, (N // 2) + 1):
        if N % i == 0:
            N = N // i
            print(i)
            break
    else:
        break

print(N)

