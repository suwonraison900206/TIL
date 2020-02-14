#  10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

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