# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
#
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)
import math

a = int(input())
k = []
for i in range(a):
    c = 0
    b = list(map(int, input().split(' ')))
    d = 0
    for number in b:
        c = c + number
    d = round(c / len(b))
    k.append(d)
for i in range(0, a):
    print('#{} {}'.format(i+1, k[i]))