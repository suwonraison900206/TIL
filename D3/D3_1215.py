import sys
sys.stdin = open("1215.txt")

for test_case in range(10):

    a = int(input())
    k = []
    for i in range(8):
        temp = list(map(str,input()))
        k.append(temp)


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = []
    cnt = 0

    for i in range(8):
        for j in range(8):


            for d in range(4):
                y = k[i][j]
                sum = []
                sum.append(y)
                di = i + dx[d]
                dj = j + dy[d]
                h = 1

                while 0 <= di < 8 and 0 <= dj < 8 and h < a:
                    sum.append(k[di][dj])
                    di = di + dx[d]
                    dj = dj + dy[d]
                    h = h + 1

                    if len(sum) == a:
                        sum1 = sum[::-1]
                        if sum == sum1:
                            cnt = cnt + 1

    print('#{} {}'.format(test_case+1,int(cnt/2)))

