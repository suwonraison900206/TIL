
a = int(input())


for i in range(1,a+1):
    cnt = 0
    if i // 100 == 3 or i // 100 == 6 or i // 100 == 9:
        cnt = cnt + 1
    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        cnt = cnt + 1
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        cnt = cnt + 1
    if cnt == 0:
        print(i, end=' ')
    else:
        print('-' * int(cnt),end='')











