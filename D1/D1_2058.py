# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

b = int(input())

c = str(b)

k = []
a = 0
for i in c:
    a = a + int(i)

print(a)