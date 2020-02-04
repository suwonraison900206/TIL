a = int(input())
k = []
for i in range(a):
    c = 0
    b = list(map(int, input().split(' ')))
    for i in b:
        if i % 2 != 0:
            c += i
    k.append(c)
for i in range(0, a):
    print('#{} {}'.format(i+1, k[i]))