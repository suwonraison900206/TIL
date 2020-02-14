# 첨에 리스트에 맥스값을 찾고

# for 문으로 하나 하나 돌려서

# 조건문으로 i 가 맥스값보다 작으면 (맥스값 - i) 값을 계속 더해주고

# 포문 끝나면 출력


#
#
#
# a = [10, 7 , 6, 11]
#
# print(a[1])
# print(a.index(7))
# print(max(a))
#
# b = max(a)
#
#
# print(a.index(b))

a = int(input())
k = []
short_c = []

for i in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    d = c[::-1] +[0]
    max = d[0]
    sum = 0

    for i in range(b):
        if d[i] < max:
            sum = sum + (max - d[i])
        else:
            max = d[i]
    k.append(sum)

for i in range(0, a):
    print('#{} {}'.format(i+1, k[i]))
