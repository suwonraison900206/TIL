#
# import sys
# sys.stdin = open("1493input.txt")
#
#


num = 270
lst = [[0 for _ in range(num)] for _ in range(num)]
lst[0][0] = 1
for i in range(1, num):
    lst[i][0] = lst[i - 1][0] + i
for i in range(num):
    for j in range(1, num):
        lst[i][j] = lst[i][j - 1] + i + j + 1
t = int(input())
print(lst)
for test_case in range(t):
    b = list(map(int, input().split()))
    X = 1
    Y = 1
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == b[0] or lst[i][j] == b[1]:
                if b[0] == b[1]:
                    X = X + (2*i)
                    Y = Y + (2*j)
                    break
                X = X + i
                Y = Y + j
                count += 1
                if count == 2:
                    break
    print('#{} {}'.format(test_case + 1,lst[X][Y]))
