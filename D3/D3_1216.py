import sys
sys.stdin = open("1216.txt")

for test_case in range(10):

    a = int(input())
    k = []
    for i in range(100):
        temp = list(map(str,input()))
        k.append(temp)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = []
    maxv = 0
    for i in range(100):
        for j in range(100):


            for d in range(2):
                y = k[i][j]
                sum = []
                sum.append(y)
                di = i + dx[d]
                dj = j + dy[d]
                h = 1

                while 0 <= di < 100 and 0 <= dj < 100 and h < 100:
                    sum.append(k[di][dj])
                    di = di + dx[d]
                    dj = dj + dy[d]
                    h = h + 1
                    sum1 = sum[::-1]

                    if sum == sum1:
                        if maxv < len(sum):
                            maxv = len(sum)




    print('#{} {}'.format(test_case+1, maxv))

