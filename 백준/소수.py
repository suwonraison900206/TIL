M = int(input())
N = int(input())
answer = []
for i in range(M, N +1):

    if i == 1:
        continue

    for j in range(2, int((i ** 0.5))+1):

        if i % j == 0:
            break

    else:
        answer.append(i)

if not answer:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])

