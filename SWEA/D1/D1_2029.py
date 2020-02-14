

a = int(input())
result = []
for i in range(1, a+1):
    b_list = list(input().split(' '))
    b1 = int(b_list[0])
    b2 = int(b_list[1])
    c1 = b1 // b2
    c2 = b1 % b2
    result.append([c1, c2])
for i in range(0, a):
    print('#{} {} {}'.format(i+1, result[i][0], result[i][1]))
