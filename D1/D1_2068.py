# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

a = int(input())
k = []
c = 0
for i in range(a):
    b = list(map(int, input().split(' ')))
    c = max(b)


    k.append((c))




for i in range(0, a):
    print('#{} {}'.format(i+1, k[i]))