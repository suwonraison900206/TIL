# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

a = int(input())
k = []
same = '='
c = '<'
d = '>'
for i in range(a):
    b = list(map(int, input().split(' ')))
    if int(b[0]) == int(b[1]):
        k.append(same)
    elif int(b[0]) > int(b[1]):
        k.append(d)
    else:
        k.append(c)
for i in range(0, a):
    print('#{} {}'.format(i+1, k[i]))